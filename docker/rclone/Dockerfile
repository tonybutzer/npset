FROM ubuntu:18.04
ENV theVersion 1.2

RUN apt-get update \
	&& apt-get install -y tzdata \
	&& apt-get install -y git \
	&& apt-get install -y make \
	&&  apt-get -y install sudo \
	&& apt-get install -y unzip  \
	&& apt-get install -y vim  \
	&& apt-get install -y curl \ 
	&& apt-get install -y awscli

RUN useradd -r -u 16108 -g 100 butzer

RUN mkdir /home/butzer && chown butzer /home/butzer \
	&& mkdir /data && chown butzer /data

WORKDIR /data
RUN curl -O https://downloads.rclone.org/rclone-current-linux-amd64.zip \
	&& unzip rclone-current-linux-amd64.zip \
	&& (cd rclone-*-linux-amd64 ; cp rclone /usr/bin/) \
	&& chown root:root /usr/bin/rclone \
	&& chmod 755 /usr/bin/rclone 

ENV theOtherVersion 1.1
USER butzer

RUN mkdir -p /home/butzer/.config/rclone
CMD /bin/bash

COPY files/Makefile /home/butzer
COPY files/rclone.conf /home/butzer/.config/rclone

WORKDIR /home/butzer
