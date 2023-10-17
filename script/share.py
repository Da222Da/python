import os

# 获取项目根目录
def get_root_directory():
    # 获取当前脚本的绝对路径
    script_path = os.path.abspath(__file__)

    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(script_path)

    # 获取项目根目录
    root_dir = os.path.dirname(script_dir)

    return root_dir

# 路径拼接 
def join(path1, path2):
    return os.path.join(path1, path2)