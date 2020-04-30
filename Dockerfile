FROM python:3

RUN apt-get update && apt-get -y install \
    libpq-dev

WORKDIR /app
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./users /app/users
ADD ./articles /app/articles
ADD ./config /app/config
ADD ./manage.py /app/

CMD ["python", "manage.py", "runserver", "0:8000"]