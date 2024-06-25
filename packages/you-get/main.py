import subprocess

if __name__ == "__main__":
    url_input = input("请输入您要下载的地址：")
    if url_input:
        subprocess.run(["you-get", "-o ~/Videos", url_input])