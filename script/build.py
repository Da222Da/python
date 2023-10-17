import share
import subprocess

root_dir = share.get_root_directory()
dist_dir = share.join(root_dir, "dist")
template_dir = share.join(root_dir, "config/nbconvert/template")
command = f"jupyter nbconvert --to html --output-dir {dist_dir} --template {template_dir} index.ipynb ./docs/**/*.ipynb"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# 检查指令是否成功运行
if result.returncode == 0:
    print("ipynb 转换 html，成功了")
else:
    print("ipynb 转换 html，失败了")