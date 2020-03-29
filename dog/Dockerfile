FROM ubuntu:16.04
MAINTAINER Tony Butzer
ENV REFRESHED_AT 2017-12-22

Volume /data

RUN apt-get -yqq update \
   &&  apt-get install -y vim \
   &&  apt-get install -y wget \
   &&  apt-get install -y python3 python3-dev python3-pip \
   &&  apt-get -y install git \
   &&  apt-get -y install dnsutils iputils-ping \
   &&  pip3 install requests \
   &&  pip3 install rq \
   && pip3 install awscli
