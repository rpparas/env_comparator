FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip --no-install-recommends
RUN apt-get install -y libmagic1

WORKDIR /usr/src/app

COPY . .
RUN pip3 install -r requirements.txt

CMD bash
