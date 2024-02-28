import logging
from logging.handlers import RotatingFileHandler
import os

class Logger(logging.Logger):
    def __init__(self, appname, name='logger', level=0, maxBytes=10*1024*1024, backupCount=10):
        super().__init__(name, level=level)
        self.log_folder = f"/var/log/{appname}"
        self.log_path = os.path.join(self.log_folder, f"{self.name.lower()}.log")

        if not os.path.exists(os.path.dirname(self.log_path)):
            os.makedirs(os.path.dirname(self.log_path), exist_ok=True)

        # Create a handler, used for output to a file
        file_handler = RotatingFileHandler(self.log_path, maxBytes=maxBytes, backupCount=backupCount)
        file_handler.setLevel(level)

        # Create a handler, used for output to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # Define the output format of handler
        formatter = logging.Formatter('%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s', datefmt='%y/%m/%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.addHandler(file_handler)
        self.addHandler(console_handler)

def create_get_child_logger(app_name):
    def get_child_logger(name):
        return Logger(app_name, name)
    return get_child_logger