# Docker

% docker, container

#platform/multiple #target/local #cat/UTILS 

## Remove an image
docker image rm <image_id>

## Delete an image from the local image store
docker rmi <image_id>

## List all images that are locally stored with the Docker engine
docker images

## Build an image from the Dockerfile in the current directory and tag the image
docker build -t <image>:<version> .

## Pull an image from a registry
docker pull <image>:<version>

# Stop a running container through SIGTERM
docker stop <container_id>

# Stop a running container through SIGKILL
docker kill <container_id>

# List the networks
docker network ls

# List the running containers
docker ps

# Delete all running and stopped containers
docker rm -f $(docker ps -aq)

# Create a new bash process inside the container and connect it to the terminal
docker exec -it <container_id> bash

# Print the last lines of a container’s logs
docker logs --tail 100 <container_id> | less

# Print the last lines of a container's logs and following its logs
docker logs --tail 100 <container_id> -f

# Create new network
docker network create <network_name>

$ image_id: docker images --- --headers 1 --column 3
$ container_id: docker ps --- --headers 1 --column 1



% docker-compose

# Builds, (re)creates, starts, and attaches to containers for all services
docker-compose up

# Builds, (re)creates, starts, and dettaches to containers for all services
docker-compose up -d

# Builds, (re)creates, starts, and attaches to containers for a service
docker-compose up -d <service_name>

# Builds, (re)creates, starts, and dettaches to containers for a service
docker-compose up -d <service_name>

# Print the last lines of a service’s logs
docker-compose logs --tail 100 <service_name> | less

# Print the last lines of a service's logs and following its logs
docker-compose logs -f --tail 100 <service_name>

# Stops containers and removes containers, networks created by up
docker-compose down

% docker, mysql
# run mysql container
docker run --rm --name=<container_name|mysql8> -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d mysql/mysql-server:<version|latest>

# connect to mysql docker container
docker exec -ti <container_name> mysql
