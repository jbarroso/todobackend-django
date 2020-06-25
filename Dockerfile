FROM python:3

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000

EXPOSE 8000
