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
 * omero.biobank.db_server

Developers can build also a custom version of the client, specifing the paths for the omero server libs and profile. See [Installing OMERO.biobank](https://github.com/crs4/omero.biobank/wiki/OMERO.biobank-installation-guide)

* `./build.sh client P1 P2`

see `./build.sh help` for more details

Running
-------

Use the 'obbdock' script to start, stop and restart the omero.biobank nodes on your machine, e.g.:

 * `./obbdock start bundle` to start the set of Omero.biobank nodes.
 * `./obbdock stop` to stop all Omero.biobank running nodes
 * `./obbdock restart cclient` to restart the Omero.biobank custom client node.

For full arguments, see `./obbdock help`