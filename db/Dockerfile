# Based on Debian Wheezy
FROM debian:wheezy
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

RUN apt-key adv --keyserver keyserver.ubuntu.com \
    --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main" > \
    /etc/apt/sources.list.d/pgdg.list

RUN apt-get update && apt-get -q -y install -q -y \
    nano \
    python-software-properties \
    software-properties-common \
    postgresql-9.3 \
    postgresql-client-9.3 \
    postgresql-contrib-9.3

USER postgres

ADD omero_db.sql /tmp/

ENV DB_USER omero 
ENV DB_PASS omero 
ENV OMERO_DB_NAME omero 
ENV OMERO_SQL_FILE /tmp/omero_db.sql

RUN sed -e 's/peer/trust/g' /etc/postgresql/9.3/main/pg_hba.conf > /tmp/pg_hba.conf 
RUN mv /tmp/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER $DB_USER WITH SUPERUSER PASSWORD '$DB_PASS';" &&\
    createdb -O $OMERO_DB_NAME $OMERO_DB_NAME &&\
    psql -U $DB_USER $OMERO_DB_NAME < $OMERO_SQL_FILE

EXPOSE 5432

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", \
    "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]