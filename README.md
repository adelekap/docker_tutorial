# DSS Team Docker Tutorial!

## Getting Started
1. Clone this repository
 
2. [Install Docker](https://docs.docker.com/v17.12/docker-for-mac/install/)

3. Run the docker engine

4. Test that everything is working

    `docker run hello-world`
    
## Simple Flask Example

1. Build the docker image

    `docker build -t docker-tutorial .`

    `docker run --name tutorial-container -p 8080:4000 docker-tutorial`

2. Check on our containers

    `docker ps -a`
    
3. Navigate to http://0.0.0.0:8080


## Multi-Container Example
 
1. Install mssql client or mssql SQLCMD

    `npm install -g sql-cli` or `brew install mssql-tools`

2. Make new docker network with the bridge driver

    `docker network create --driver bridge sql-net`

3. Spin up the container with the volumes mapped

    `docker run --name sql-container --env="ACCEPT_EULA=Y" --env="SA_PASSWORD=reallyStrongPwd123" --network=sql-net  -p 1433:1433 --detach microsoft/mssql-server-linux:latest`
    
4. Build the docker-tutorial image and start the container

    `docker build -t docker-tutorial-sql .`
    
    `docker run --name flask-container -p 8080:4000 --network sql-net docker-tutorial-sql`

5. Navigate to http://0.0.0.0:8080/search/<your_fun_query>

6. Then try saving the result in the DB by navigating to http://0.0.0.0:8080/search/<your_fun_query>/store-result

7. Check the database for the added record!

    with sql client:

    `mssql -u sa -p reallyStrongPwd123 --port 1433`
    
    `USE DemoDB; SELECT * FROM SearchResults;`
    
    or with sqlcmd:
    
    `sqlcmd -S localhost -U sa -P reallyStrongPwd123 -Q "USE DemoDB; SELECT * FROM SearchResults;"`


## Using Volumes

1. Create a volume

    `docker volume create mssqlsystem`

2. Spin up the container with the volumes mapped

    `docker run --name sql-container --volume mssqlsystem:/var/opt/mssql --env="ACCEPT_EULA=Y" --env="SA_PASSWORD=reallyStrongPwd123" --network=sql-net  -p 1433:1433 -d microsoft/mssql-server-linux:latest`
    
3. Run (or start) the flask server container
    
    `docker run --name flask-container -p 8080:4000 --network sql-net -d docker-tutorial-sql`
    
    `docker start flask-container`
    
## Docker Compose

1. Define services in a compose file [docker-compose.yml](./sql_server_example/docker-compose.yml)

2. Build and run app with Compose

    `docker-compose up`

    
## Other helpful docker commands!

#### current docker status
`docker info`

#### remove a container
`docker container rm <name of container>`

#### kill all containers
`docker kill $(docker ps -q)`

#### run command in an active container
`docker exec -it <name of container> bash`

#### remove all unused images/containers/volumes
`docker system prune`

#### view container logs
`docker logs <name of container>`

[and more](https://docs.docker.com/engine/reference/commandline/docker/)...


### [portainer](https://www.portainer.io/)
