# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /usr/src/app

RUN apt update && apt install -y python3-opencv

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY target.py .

ENTRYPOINT [ "python", "target.py" ]
