# Django REST API with AWS ECS

## Get started

```
$ source ./env/bin/activate
```

## Create a user

```
$ python manage.py createsuperuser
$ python manage.py makemigrations
$ python manage.py migrate
```

## Run

```
$ python manage.py runserver
```

## Testing

```
$ curl -i http://127.0.0.1:8000/users/
```