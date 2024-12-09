
def merge_dict(dict1, dict2):
    for key in dict2:
        if isinstance(dict2[key], dict):
            if key not in dict1:
                dict1[key] = {}
            merge_dict(dict1[key], dict2[key])
        elif isinstance(dict2[key], list):
            if key not in dict1:
                dict1[key] = []
            dict1[key].extend(dict2[key])
        else:
            dict1[key] = dict2[key]

def log_error(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            self.log.error(str(e))
    return wrapper


def get_device_tree_path():
    """
    获取设备树路径。
    
    Returns:
        str: 设备树路径，如果不存在则返回None。
    """
    from os import path
    device_tree_path = '/proc/device-tree'
    if not path.exists(device_tree_path):
        device_tree_path = '/device-tree'
        if not path.exists(device_tree_path):
            return None
    return device_tree_path

def get_hat_version():
    """
    获取HAT设备的版本号。
    
    如果未发现HAT设备或发生错误，则返回错误码。
    
    Returns:
        int: HAT版本号或错误码。
    """
    from os import listdir, path
    device_tree_path = get_device_tree_path()
    product_ver = 0
    if device_tree_path is None:
        return product_ver
    hat_path = None
    for file in listdir(device_tree_path):
        if file.startswith('hat'):
            hat_path = f"{device_tree_path}/{file}"
            break
    if hat_path is None:
        return product_ver
    product_ver_file = f"{hat_path}/product_ver"
    if not path.exists(product_ver_file):
        return product_ver
    try:
        with open(product_ver_file, "r") as f:
            product_ver = f.read().strip()
            product_ver = int(product_ver, 16)
    except Exception as e:
        pass
    
    return product_ver

def get_hat_version():
    return 10