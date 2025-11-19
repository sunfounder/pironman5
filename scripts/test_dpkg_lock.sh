#!/bin/bash

# 测试脚本：手动模拟dpkg锁被占用的场景
# 用法：在一个终端运行此脚本，然后在另一个终端运行wait_for_dpkg.sh

echo "开始模拟dpkg锁被占用的情况..."
echo "运行10秒后自动释放锁"

# 定义dpkg锁文件路径
DPKG_LOCK="/var/lib/dpkg/lock"
LOCK_FRONTEND="/var/lib/dpkg/lock-frontend"
APT_LOCK="/var/lib/apt/lists/lock"

# 检查是否有足够权限
if [ "$EUID" -ne 0 ]; then
  echo "此脚本需要以root权限运行，因为dpkg锁文件需要root权限才能创建"
  echo "请使用 sudo 运行此脚本"
  exit 1
fi

# 模拟占用dpkg锁
function lock_dpkg() {
  # 尝试以写入模式打开锁文件并保持打开状态
  # 这会模拟一个进程正在使用dpkg
  echo "正在获取dpkg锁..."
  
  # 在后台打开锁文件
  { 
    exec 9> "$DPKG_LOCK" 2>/dev/null
    exec 10> "$LOCK_FRONTEND" 2>/dev/null
    exec 11> "$APT_LOCK" 2>/dev/null
    
    # 显示已获取的锁
    echo "已获取的锁:"
    [ -e "$DPKG_LOCK" ] && echo "- $DPKG_LOCK"
    [ -e "$LOCK_FRONTEND" ] && echo "- $LOCK_FRONTEND"
    [ -e "$APT_LOCK" ] && echo "- $APT_LOCK"
    
    echo "模拟PackageKit进程占用dpkg锁..."
    echo "在另一个终端运行: sudo ./wait_for_dpkg.sh 来测试"
    
    # 保持锁10秒
    sleep 10
    
    # 释放锁
    echo "正在释放锁..."
    exec 9>&-
    exec 10>&-
    exec 11>&-
    
    echo "锁已释放"
  } &
  
  # 保存后台进程PID
  LOCK_PID=$!
  echo "锁占用进程PID: $LOCK_PID"
  echo "按 Ctrl+C 可提前终止并释放锁"
}

# 清理函数
trap cleanup SIGINT SIGTERM

function cleanup() {
  echo "\n正在清理..."
  if [ -n "$LOCK_PID" ] && ps -p "$LOCK_PID" > /dev/null; then
    kill "$LOCK_PID" > /dev/null 2>&1
    wait "$LOCK_PID" 2>/dev/null
  fi
  echo "测试结束"
  exit 0
}

# 开始测试
lock_dpkg

# 等待后台进程完成
wait $LOCK_PID

echo "测试完成"
exit 0