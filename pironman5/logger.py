import logging
from logging.handlers import RotatingFileHandler
import os

# 添加颜色代码定义
class ColoredFormatter(logging.Formatter):
    COLOR_CODES = {
        'DEBUG': '\033[94m',    # 蓝色
        'INFO': '\033[92m',     # 绿色
        'WARNING': '\033[93m',  # 黄色
        'ERROR': '\033[91m',    # 红色
        'CRITICAL': '\033[95m'  # 紫色
    }
    RESET_CODE = '\033[0m'     # 重置颜色

    def format(self, record):
        levelname = record.levelname
        color_code = self.COLOR_CODES.get(levelname, '')
        reset_code = self.RESET_CODE if color_code else ''
        # 添加颜色代码并保留原始格式
        record.levelname = f'{color_code}{levelname}{reset_code}'
        return super().format(record)

class Logger(logging.Logger):
    def __init__(self, appname, level=0, maxBytes=100*1024*1024, backupCount=5):
        super().__init__(appname, level=level)
        self.log_folder = f"/var/log/{appname}"
        self.log_path = os.path.join(self.log_folder, f"{appname.lower()}.log")

        # Create a handler, used for output to a file
        file_handler = RotatingFileHandler(self.log_path, maxBytes=maxBytes, backupCount=backupCount)
        file_handler.setLevel(level)

        # Create a handler, used for output to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # Define the output format of handler
        file_logger_formatter = logging.Formatter('%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s', datefmt='%y/%m/%d %H:%M:%S')
        console_logger_formatter = ColoredFormatter('[%(levelname)s] %(message)s')
        file_handler.setFormatter(file_logger_formatter)
        console_handler.setFormatter(console_logger_formatter)

        # Add the handler to the logger
        self.addHandler(file_handler)
        self.addHandler(console_handler)

    def setLevel(self, level):
        super().setLevel(level)
        for handler in self.handlers:
            handler.setLevel(level)
