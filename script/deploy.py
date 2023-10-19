import share
import subprocess

root_dir = share.get_root_directory()
dist_dir = share.join(root_dir, "dist")



# 初始化
def init():
    return ""

# 打包项目
def build():
    script_dir = share.join(root_dir, "script/build.py")
    return subprocess.run(["python", script_dir])

# 发布到 github
def github():
    commands = [
        'git init',
        'git add --all',
        'git commit -m "deploy"',
        'git remote add origin git@github.com:Da222Da/python.git',
        'git push -f git@github.com:Da222Da/python.git master:gh-pages',
    ]    
    for item in commands:
        result = subprocess.run(item, shell=True, capture_output=True, text=True, cwd=dist_dir)
        if result.returncode != 0:
            print(result.stdout or result.stderr)
            break

# 主程序
def main():
    init()
    build()
    github()

main()