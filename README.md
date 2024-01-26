# 4DESA
## Getting started

### Use docker to install deploy local postgres server
 ```cmd
 docker run --name some-postgres -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres
 ```
### Install project virtual env and packages with poetry
```cmd
cd {project_root}
```
_cd into project root_
```cmd
where python
```
_locate diffrent python executables, choose a python executable that is at least in version **3.12.0**_
```cmd
where python
```
_install poetry_
```cmd
{python3.12_executable_path}\python.exe -m pip install poetry 
```
_install virtual env and packages with **poetry**_
```cmd
{python3.12_executable_path}\python.exe -m poetry install
```

## Poetry's workflow
Poetry is used in this project to handle virtual environments and index requirements precisely. 
Do take a look at the projects manifests (_pyproject.toml_/_poetry.lock_) that will not explain further here but as all ways, you owe it to yourself to [**read the docs**](https://python-poetry.org/).

### open virtual env shell
To execute commands in the poetry virtual environment, you can either enter the shell of the virtual environment and then execute any batch/bash command:
```cmd
{python3.12_executable_path}\python.exe -m poetry shell
```
Or send commands to the virtual environment from your current environment:
```cmd
{python3.12_executable_path}\python.exe -m poetry run {any_command}
```
The finality is the same, do as you prefer.

### add a new package
Just like you would `pip install` some package, you can `poetry add` them.
```cmd
{python3.12_executable_path}\python.exe -m poetry add {some_package}
```
This has the added beninfit of updating the porject manifests (`pyproject.toml`/`poetry.lock`) and takes into account the current project dependencies when installing one version on the desired packege over an other.

### remove a package
Basicly the opposite of adding a package.

```cmd
{python3.12_executable_path}\python.exe -m poetry remove {some_package}
```








**Have fun and never use venv, pipenv or any other crap like that again!**


