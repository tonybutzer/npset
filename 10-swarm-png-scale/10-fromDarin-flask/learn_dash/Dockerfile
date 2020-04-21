FROM ubuntu:18.04
ENV theVersion 1.6

RUN apt-get update && apt-get install -y git && apt-get install -y make \
	&&  apt-get install -y python3-pip \
   	&&  apt-get -y install dnsutils \
   	&&  apt-get -y install curl \
   	&&  pip3 install awscli

USER root
CMD /bin/bash

RUN mkdir -p /opt 
WORKDIR /opt

RUN mkdir -p /opt/run
WORKDIR /opt/run
COPY requirements.txt /opt/run
RUN pip3 install -r requirements.txt
COPY app.py /opt/run
CMD ["/usr/bin/python3", "app.py"]
#CMD ["./sleepy.sh"]
