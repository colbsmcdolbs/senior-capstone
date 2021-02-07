FROM python:3.8-slim

RUN mkdir /usr/src/app/

COPY . /usr/src/app/

WORKDIR /usr/src/app/

EXPOSE 5000

COPY requirements.txt /usr/src/app/

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

CMD ["python", "app.py"]
