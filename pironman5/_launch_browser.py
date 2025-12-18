#!/usr/bin/env python3
import subprocess
import sys
import os
from typing import Optional, List

def check_desktop_environment() -> bool:
    """
    检测当前是否处于桌面环境（防止SSH/纯控制台环境执行失败）
    返回：True=桌面环境，False=非桌面环境
    """
    # 核心检测项1：DISPLAY环境变量（X11/Wayland必备）
    if not os.getenv("DISPLAY"):
        print("错误：未检测到DISPLAY环境变量，当前可能是SSH/纯控制台环境", file=sys.stderr)
        return False
    
    # 核心检测项2：会话类型（区分桌面/控制台）
    session_type = os.getenv("XDG_SESSION_TYPE", "")
    if session_type not in ["x11", "wayland"]:
        print(f"错误：当前会话类型为{session_type}，仅支持x11/wayland桌面会话", file=sys.stderr)
        return False
    
    # 可选检测：确认存在桌面环境标识（GNOME/KDE/XFCE等）
    desktop_env = os.getenv("XDG_CURRENT_DESKTOP", "")
    if not desktop_env:
        print("警告：未检测到明确的桌面环境标识（如GNOME/KDE），可能无法正常打开浏览器", file=sys.stderr)
        # 此处仅警告不退出，部分极简桌面可能无该变量
    
    return True

def find_available_browsers() -> List[str]:
    """
    检测系统中已安装的浏览器，返回可执行命令列表
    优先级：chromium > google-chrome > firefox
    """
    browsers = [
        "chromium-browser",  # Debian/Ubuntu 系 Chromium
        "chromium",          # 通用 Chromium
        "google-chrome",     # Google Chrome
        "google-chrome-stable",  # Chrome 稳定版
        "firefox"            # Firefox
    ]
    
    available = []
    for browser in browsers:
        # 使用 which 命令检查是否安装
        try:
            subprocess.run(
                ["which", browser],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            available.append(browser)
        except subprocess.CalledProcessError:
            continue
    
    return available

def get_browser_fullscreen_args(browser: str) -> List[str]:
    """
    根据不同浏览器返回对应的全屏参数
    """
    target_url = "http://127.0.0.1:34001"
    
    # Chrome/Chromium 全屏参数
    if "chrome" in browser or "chromium" in browser:
        return [
            browser,
            "--start-fullscreen",  # 启动即全屏
            "--kiosk",             # 自助终端模式（无地址栏/菜单）
            "--no-first-run",      # 跳过首次运行引导
            "--no-default-browser-check",  # 跳过默认浏览器检测
            target_url
        ]
    # Firefox 全屏参数
    elif "firefox" in browser:
        return [
            browser,
            "-kiosk",              # 全屏自助终端模式
            "-new-window",         # 打开新窗口
            target_url
        ]
    else:
        return [browser, target_url]

def launch_browser() -> bool:
    """
    启动浏览器并全屏打开指定页面
    返回：是否成功启动
    """
    # 查找可用浏览器
    available_browsers = find_available_browsers()
    if not available_browsers:
        print("错误：未检测到任何支持的浏览器（Chrome/Chromium/Firefox）", file=sys.stderr)
        return False
    
    # 使用第一个找到的浏览器
    selected_browser = available_browsers[0]
    print(f"检测到可用浏览器：{selected_browser}")
    
    # 构建启动命令
    cmd = get_browser_fullscreen_args(selected_browser)
    print(f"执行命令：{' '.join(cmd)}")
    
    try:
        # 后台启动浏览器（不阻塞脚本，独立运行）
        subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        print(f"成功启动 {selected_browser}，已全屏打开 {cmd[-1]}")
        return True
    except Exception as e:
        print(f"启动浏览器失败：{str(e)}", file=sys.stderr)
        return False

def run():
    """主函数"""
    # 1. 检查是否为Linux系统
    if not sys.platform.startswith("linux"):
        print("错误：此脚本仅支持Linux系统", file=sys.stderr)
        sys.exit(1)
    
    # 2. 新增：检查是否为桌面环境（核心修改）
    if not check_desktop_environment():
        sys.exit(1)
    
    # 3. 警告：避免root权限运行
    if os.geteuid() == 0:
        print("警告：不建议使用root权限运行浏览器，可能导致权限/安全问题", file=sys.stderr)
    
    # 4. 启动浏览器
    if not launch_browser():
        sys.exit(1)

if __name__ == "__main__":
    run()