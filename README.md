# Django REST API with AWS ECS

## Install pyenv as environment

```bash
$ brew install pyenv
$ pyenv install 3.7.0
$ pyenv global 3.7.0
$ pip install --upgrade pip
```
> https://github.com/pyenv/pyenv

## Install project

```bash
$ git clone https://github.com/milerDev/miler-api
$ cd miler-api
$ python -m venv env
$ . env/bin/activate

(env)
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```

`.vscode/settings.json`
```
{
    "python.pythonPath": "/Users/minhyeokjung/.pyenv/versions/3.7.0/bin/python",
    "python.linting.pylintEnabled": true,
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true
}
```

## Configure a django application

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Run

```
$ python manage.py runserver
```

## Testing

```
$ curl -i http://127.0.0.1:8000/users/
```

## Docker

```bash
$ docker-compose -f docker-compose-pg.yml up -d # PostgresSQL only
$ docker-compose up -d --build
$ docker-compose exec django ./manage.py test
```

```bash
$ docker build -t miler-api .
$ docker run miler-api
```