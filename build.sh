#! /bin/bash

# Omero.biobank client details
CLIENT_PATH=`pwd`/client
CLIENT_IMAGE_NAME="omero.biobank.client"
CLIENT_CONTAINER_NAME="obb_client"

# Omero.biobank custom client details
CUSTOM_CLIENT_IMAGE_NAME="omero.biobank.custom_client"
CUSTOM_CLIENT_CONTAINER_NAME="obb_custom_client"

# Omero.biobank server details
SERVER_PATH=`pwd`/server
SERVER_IMAGE_NAME='omero.biobank.server'
SERVER_CONTAINER_NAME='obb_server'

# Database server details
DB_PATH=`pwd`/db
DB_IMAGE_NAME='omero.biobank.db.server'
DB_CONTAINER_NAME='obb_db_server'

CONTAINERS=($CUSTOM_CLIENT_CONTAINER_NAME $CLIENT_CONTAINER_NAME $SERVER_CONTAINER_NAME $DB_CONTAINER_NAME)
IMAGES=($CUSTOM_CLIENT_IMAGE_NAME $CLIENT_IMAGE_NAME $SERVER_IMAGE_NAME $DB_IMAGE_NAME)
DOCKERS_PATHS=($CLIENT_PATH $SERVER_PATH $DB_PATH)

DOCKER=`which docker.io`
if [[ "$DOCKER" == "" ]]; then
    DOCKER=`which docker`
fi
DOCKER_BUILD="$DOCKER build -q --rm=true"

function usage {
    echo >&2
    echo >&2 "usage: $0 argument(s)"
    echo >&2    
    echo >&2
    echo >&2 "arguments list:"
    echo >&2 "  bundle            Build Omero.biobank client, server, db nodes"    
    echo >&2 "  clean             Remove all build information"
    echo >&2 "  clean containers  Remove containers information"
    echo >&2 "  clean support     Remove build support information"
    echo >&2 "  client            Build Omero.biobank client node"
    echo >&2 "  client P1 P2      Build custom Omero.biobank client node"
    echo >&2 "                      P1 path to omero lib"
    echo >&2 "                      P2 path to omero server profile"
    
}


function build_image {
    local path=$1
    local image=$2
    local support_path=$path/support
    
    cd $path
    if [ -d $support_path ];then
	rm -rf $support_path
    fi
    mkdir $support_path

    if [[ "$image" == $CLIENT_IMAGE_NAME ]]; then
	# use files from omero.biobank.server docker image
	cp -r server_lib/ $support_path/omero_lib
	cp obb_server.profile $support_path/omero.biobank.server.profile
    fi

    if [[ "$image" == $CUSTOM_CLIENT_IMAGE_NAME ]]; then
	local omero_lib_path=$3
	local omero_server_profile=$4
  
	if [ -d $omero_lib_path ]; then
	    cp -r $omero_lib_path $support_path/omero_lib
	else
	    echo >&2 " No $omero_lib_path directory found"
	    exit 0
	fi
	
	if [ -f $omero_server_profile ]; then
	    cp $omero_server_profile $support_path/omero.biobank.server.profile 
	else
	    echo >&2 " No $omero_server_profile file found"
	    exit 0
	fi
    fi  

  $DOCKER_BUILD -t $image .
  echo "*** "
  echo "*** Successfully built $image ***"
  echo "*** "
}

function rm_container {
    local container=$1
    echo "Stopping container $container"
    $DOCKER stop $container #2>/dev/null
    echo "Removing container $container"
    $DOCKER rm $container #2>/dev/null
}


function rm_image {
    local image=$1
    echo "Removing image $image"
    $DOCKER rmi $image #2>/dev/null
}


if [ "$1" = '' ] || [ "$1" = '-h' ] || [ "$1" = 'help' ]; then
  usage
  exit 1
fi

if [ "$1" = 'clean' ]; then
    rm_containers=false
    rm_images=false
    rm_support=false

    if [ ! -z "$2" ] && [ "$2" = 'containers' ]; then
	rm_containers=true
    elif  [ ! -z "$2" ] && [ "$2" = 'support' ]; then
	rm_support=true
    else
	rm_containers=true
	rm_images=true
	rm_support=true
    fi

    if [[ $rm_containers == true ]] 
    then
	for c in ${CONTAINERS[*]}; do
	    rm_container $c
	done
    fi
    if [[ $rm_images == true ]] 
    then
	for i in ${IMAGES[*]}; do
	    rm_image $i
	done
    fi
    if [[ $rm_support == true ]] 
    then
	for p in ${DOCKERS_PATHS[*]}; do
	    cd $p
	    echo "Removing $p/support"
	    rm -rf $p/support
	done
    fi
fi

if [ "$1" = 'bundle' ]; then
    build_image $DB_PATH $DB_IMAGE_NAME
    build_image $SERVER_PATH $SERVER_IMAGE_NAME
    build_image $CLIENT_PATH $CLIENT_IMAGE_NAME	
fi

if [ "$1" = 'client' ]; then
    if [ -z "$2" ] && [ -z "$3" ]; then
	build_image $CLIENT_PATH $CLIENT_IMAGE_NAME   
    elif [ ! -z "$2" ] && [ ! -z "$3" ]; then
	build_image $CLIENT_PATH $CUSTOM_CLIENT_IMAGE_NAME $2 $3
    else
	usage
    fi     
fi



