# Based on Debian Wheezy
FROM gmauro/oracle-java
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -q -y install -q -y \
    git \
    postgresql-contrib \
    supervisor

RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN apt-get update && \
    apt-get -q -y install -q -y \
    python-imaging \
    python-matplotlib \
    python-numpy \
    python-pip \
    python-scipy \
    python-tables \
    python-virtualenv \
    python-dev \
    ipython \
    ice-services \
    python-zeroc-ice 
    

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:iliade' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN useradd -m omero -s /bin/bash \
    && chmod a+X ~omero \
    && echo 'omero:omero' | chpasswd


RUN mkdir -p "/OMERO" \
    && chown omero "/OMERO"

USER omero

RUN cd /home/omero/ \
    && git clone --recursive git://github.com/openmicroscopy/openmicroscopy.git \
    && mv openmicroscopy ome \
    && cd ome \
    && git checkout -b master origin/master \
    && git reset --hard v.4.4.12 \
    && git submodule update

RUN cd /home/omero/ \
    && git clone https://github.com/crs4/omero.biobank \
    && cd omero.biobank \
    && git checkout develop 

RUN cp /home/omero/omero.biobank/models/*.ome.xml \
    /home/omero/ome/components/model/resources/mappings/

RUN /home/omero/omero.biobank/utils/patch_ome_config \
    --ome-home /home/omero/ome/ \
    --models-repository  /home/omero/omero.biobank/models/

RUN echo 'omero.biobank.graph.engine=pygraph' >> \
    /home/omero/ome/etc/omero.properties \
    &&  echo 'omero.biobank.messages_queue.enabled=False' >> \
    /home/omero/ome/etc/omero.properties

RUN sed -e 's/-Djavac.maxmem.default=750M/-Djavac.maxmem.default=1024M/g' \
    /home/omero/ome/build.py > /home/omero/ome/build_.py \
    && mv /home/omero/ome/build_.py /home/omero/ome/build.py \
    && chmod a+x /home/omero/ome/build.py

RUN /home/omero/ome/build.py \
    && /home/omero/ome/build.py build-schema \ 
    -Domero.db.dialect=org.hibernate.dialect.PostgreSQLDialect 
   
ENV PATH /home/omero/ome/dist/bin/:$PATH

RUN omero config set omero.data.dir "/OMERO" \
    && omero config set omero.db.host "db_server" \
    && omero config set omero.db.name "omero" \
    && omero config set omero.db.user "omero" \
    && omero config set omero.db.pass "omero" 

RUN omero db script -f /home/omero/ome/etc/omero_db.sql "" "" "omero"

ADD ./omero /omero

EXPOSE 22 4063 4064

VOLUME  ["/home/omero/ome/", "/OMERO/"]

USER root
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisord.conf"]