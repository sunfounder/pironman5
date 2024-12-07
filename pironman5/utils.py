
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


def get_hat_version():
    from os import listdir, path
    hat_path = None
    device_tree_path = '/proc/device-tree'
    if not path.exists(device_tree_path):
        device_tree_path = '/device-tree'
        if not path.exists(device_tree_path):
            return 10
    for file in listdir(device_tree_path):
        if file.startswith('hat'):
            hat_path = f"{device_tree_path}/{file}"
            break
    product_ver = 0
    with open(f"{hat_path}/product_ver", "r") as f:
        product_ver = f.read()[:-1]
        product_ver = int(product_ver, 16)
    
    return product_ver
