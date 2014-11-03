# Based on Debian Wheezy
FROM debian:wheezy
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

# Install prerequisite packages for Omero.biobank client

RUN apt-get update && \
    apt-get -q -y install -q -y \
    git \
    libicessl34 \
    python \
    python-minimal \
    python-pip \
    ipython \
    python-zeroc-ice \
    python-numpy \
    python-pika \
    python-pygraph 

RUN pip install bulbs voluptuous

RUN apt-get update && \
    apt-get install -y openssh-server

RUN mkdir /var/run/sshd
RUN echo 'root:iliade' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN mkdir -p /opt/omero/lib
ADD support/omero_lib /opt/omero/lib
ENV PYTHONPATH /opt/omero/lib
RUN echo 'export PYTHONPATH="/opt/omero/lib"' >> /etc/bash.bashrc

ADD support/omero.biobank.server.profile /opt/
RUN cat /opt/omero.biobank.server.profile >> /etc/bash.bashrc

RUN cd /opt \
    && git clone https://github.com/crs4/omero.biobank \
    && cd omero.biobank \
    && git checkout develop \
    && python setup.py install


EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
