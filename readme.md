# Startup
## requirements
_our project uses python3.12 and docker._

## run the docker container
```sh
cd {project_root} && docker compose up -d
```

## run the django web app
```sh
python -m pip install poetry
```
```sh
python -m poetry install
```
```sh
python -m poetry run python manage.py makemigrations
```
```sh
python -m poetry run python manage.py migrate
```
```sh
python -m poetry install
```
```sh
python -m poetry run python manage.py runserver
```