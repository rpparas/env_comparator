FROM python:3.6-slim
WORKDIR /usr/src/app

COPY . .
RUN pip3 install -r requirements.txt

CMD bash
