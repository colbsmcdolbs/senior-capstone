FROM python:3.8-slim

ADD requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

ADD . /app

EXPOSE 8080

CMD ["python", "app.py"]