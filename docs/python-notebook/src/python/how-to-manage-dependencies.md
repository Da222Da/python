# 在多人共同合作的项目中，如何确保第三方包被统一管理呢？

## pipenv 

`pipenv` 是一个Python项目的依赖管理工具，它结合了 `pip` 和 `virtualenv` 的功能，并提供了更简单和一致的方式来管理项目的依赖项和虚拟环境。

要使用 `pipenv` ，您可以按照以下步骤进行操作：

1. 安装 `pipenv` ：打开终端或命令提示符，运行以下命令使用pip安装 `pipenv` ：

```sh
pip install pipenv
```

2. 创建新项目：进入您的项目目录，并运行以下命令以创建一个新的 `pipenv` 环境并初始化项目：
```sh
pipenv --python 3.11.4
```
这将创建一个基于Python 3.9的虚拟环境，并在项目目录中生成一个 `Pipfile` 文件，用于管理项目的依赖项。

3. 安装依赖项：使用 `pipenv` 安装您的项目所需的依赖项。例如，运行以下命令以安装 `requests` 包：
```sh
pipenv install requests # pipenv sync
```
`pipenv` 将自动安装 `requests` 包并将其添加到 `Pipfile` 中。

4. 运行项目：使用 `pipenv` 运行您的项目。例如，运行以下命令来启动Python解释器并进入项目的虚拟环境：
```sh
pipenv shell  # 激活虚拟环境
pipenv --venv # 查看虚拟环境信息
```
然后，您可以运行项目的Python脚本或启动应用程序`pipenv run index.py`。

5. 协作和部署： `pipenv` 还提供了一些命令来协作和部署项目。例如，您可以使用 `pipenv lock` 命令锁定依赖项的版本，并生成一个 `Pipfile.lock` 文件，以确保在不同环境中使用相同的依赖项版本。您还可以使用 `pipenv sync` 命令安装或更新项目的所有依赖项。

这些是使用 `pipenv` 的基本步骤。它提供了一种简化和集成的方式来管理Python项目的依赖项和虚拟环境，使项目的开发和部署更加方便和可靠。