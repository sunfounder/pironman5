# from pironman5 import varient_id, \
#     version, \
#     VARIENT, \
#     NAME, \
#     ID, \
#     PRODUCT_VERSION, \
#     PERIPHERALS, \
#     SYSTEM_DEFAULT_CONFIG, \
#     DT_OVERLAYS

# print(f'varient_id: {varient_id}, version: {version}')
# print(f'VARIENT: {VARIENT}')
# print(f'NAME: {NAME}')
# print(f'ID: {ID}')
# print(f'PRODUCT_VERSION: {PRODUCT_VERSION}')    
# print(f'PERIPHERALS: {PERIPHERALS}')
# print(f'SYSTEM_DEFAULT_CONFIG: {SYSTEM_DEFAULT_CONFIG}')
# print(f'DT_OVERLAYS: {DT_OVERLAYS}')

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

def read_device_tree_file(file_path):
    from os import path
    if not path.exists(file_path):
        return None
    with open(file_path, "r") as f:
        result = f.read()[:-1]
        result = int(result, 16)
        return result

def get_part_number():
    """
    获取HAT设备的版本号。
    
    如果未发现HAT设备或发生错误，则返回错误码。
    
    Returns:
        str: HAT设备的PN号。
    """
    from os import listdir
    device_tree_path = get_device_tree_path()
    part_number = ""
    if device_tree_path is None:
        return
    hat_path = None
    for file in listdir(device_tree_path):
        if file.startswith('hat'):
            hat_path = f"{device_tree_path}/{file}"
            break
    if hat_path is None:
        return
    product_id_file = f"{hat_path}/product_id"
    product_ver_file = f"{hat_path}/product_ver"

    try:
        product_id = read_device_tree_file(product_id_file)
        product_ver = read_device_tree_file(product_ver_file)
        if product_id is None or product_ver is None:
            return
        part_number = f"{product_id:04d}V{product_ver:02d}"
    except Exception as e:
        # print(f"Error: {e}")
        pass
    
    return part_number

print(f'part_number: {get_part_number()}')