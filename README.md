# DSS Team Docker Tutorial!

## Getting Started
1. Clone this repository
 
2. [Install Docker](https://docs.docker.com/v17.12/docker-for-mac/install/)

3. Run the docker engine

4. Test that everything is working

    `docker run hello-world`
    
## Simple Flask Example

1. Build the docker image

    `docker build -t docker-tutorial`

    `docker run --name tutorial-container -p 8080:4000 docker-tutorial`

2. Check on our containers

    `docker ps -a`


## Two Containers Example
 
1. Install mssql client

    `npm install -g sql-cli`

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

    `mssql -u sa -p reallyStrongPwd123 --port 1433`
    
    `USE DemoDB; SELECT * FROM SearchResults;`


## Using Volumes

1. Create two volumes

    `docker volume create mssqlsystem`
    
    `docker volume create mssqluser`

2. Spin up the container with the volumes mapped

    `docker run --name sql-container --volume mssqlsystem:/var/opt/mssql --volume mssqluser:/var/opt/sqlserver --env="ACCEPT_EULA=Y" --env="SA_PASSWORD=reallyStrongPwd123" --network=sql-net  -p 1433:1433 --detach microsoft/mssql-server-linux:latest`
    
3. Build the docker-tutorial image and start the container

    `docker build -t docker-tutorial-sql`
    
    `docker run --name flask-container -p 8080:4000 --network sql-net docker-tutorial-sql`
    
## Other helpful docker commands!

#####current docker status
`docker info`

#####remove a container
`docker container rm <name of container>`

#####remove all exited containers
`docker ps -a -f status-exited`

#####run command in an active container
`docker exec -it <name of container> bash`

#####remove all unused images/containers/volumes
`docker system prune`

#####remove volume
`docker volume rm <name of volume>`

[and more](https://docs.docker.com/engine/reference/commandline/docker/)...