FROM ubuntu:18.04
ENV theVersion 1.6

RUN apt-get update && apt-get install -y git && apt-get install -y make &&  apt-get -y install sudo && \
	apt-get install -y software-properties-common && \
	apt-get install -y vim && \
	apt-get install -y ca-certificates && \
	apt-get install -y python3-pip \
	&&  apt-get -y install locales \
 	&&  apt-get install -y nmap \
   	&&  apt-get -y install traceroute \
   	&&  apt-get -y install net-tools \
   	&&  apt-get -y install dnsutils \
   	&&  apt-get -y install iputils-ping \
   	&&  apt-get -y install curl \
   	&&  pip3 install requests \
   	&&  pip3 install rq \
   	&&  pip3 install awscli

# Fix an issue with libcurl...
RUN mkdir -p /etc/pki/tls/certs \
	&& ln -s /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt;

USER root
CMD /bin/bash


RUN mkdir -p /opt 
WORKDIR /opt

ENV cloneVersion 2.5
RUN git clone https://github.com/tonybutzer/npset

WORKDIR /opt/npset/mylib/playLib
RUN make build-root

# Set the locale
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

RUN mkdir -p /opt/run \
    && mkdir -p /opt/run/junkbox
WORKDIR /opt/run
COPY requirements.txt /opt/run
RUN pip3 install -r requirements.txt
COPY q_spawner.py /opt/run
COPY cogxfer.py /opt/run
COPY breed.py /opt/run
COPY config_cogxfer.json /opt/run
COPY sleepy.sh /opt/run
CMD ["/usr/bin/python3", "q_spawner.py"]
#CMD ["./sleepy.sh"]
