import subprocess

result = subprocess.run("jupyter notebook", shell=True, capture_output=True, text=True)

# 检查指令是否成功运行
if result.returncode == 0:
    print("运行成功")
else:
    print("运行失败")