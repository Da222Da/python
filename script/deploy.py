import share
import subprocess

root_dir = share.get_root_directory()
script_dir = share.join(root_dir, "script/build.py")
result = subprocess.run(["python", script_dir])

if result.returncode == 0:
    dist_dir = share.join(root_dir, "dist")
    commands = [
        f'cd {dist_dir}',
        'git init',
        'git add --all',
        'git commit -m "deploy"',
        'git remote add origin git@github.com:Da222Da/python.git',
        'git push -f git@github.com:Da222Da/python.git master:gh-pages',
        f'rm -rf {dist_dir}'
    ]
    for item in commands:
        result = subprocess.run(item, shell=True, capture_output=True, text=True)
        print(result)
        if result.returncode != 0:
            print("Error")
            break