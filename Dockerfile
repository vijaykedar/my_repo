FROM python:3.7-slim
WORKDIR /studentproject
ADD . /studentproject
RUN apt-get install mariadb-server mariadb-client -y 
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000
