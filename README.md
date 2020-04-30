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
$ pip install -r requirement.txt
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
$ docker-compose up -d --build
$ docker-compose exec django ./manage.py test
```

```bash
$ docker build -t miler-api .
$ docker run miler-api
```