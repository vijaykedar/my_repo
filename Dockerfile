FROM python:3.7.16-slim-bullseye
WORKDIR /studentproject
ADD . /studentproject
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
