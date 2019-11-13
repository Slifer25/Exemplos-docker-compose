FROM python:3.7

COPY src /opt/application

WORKDIR /opt/application

RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0


