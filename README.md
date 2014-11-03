omero.biobank-docker
====================

Docker setup for http://github.com/crs4/omero.biobank

Prerequisites
-------------

* Docker

Install Docker. [Installation Guides](https://docs.docker.com/installation/#installation)

Building
--------

Type `./build.sh bundle` to build the following Docker images:

 * omero.biobank.client
 * omero.biobank.server
 * db_server

Running
-------

Use the 'obbdock' script to start, stop and restart the omero.biobank nodes on your machine.