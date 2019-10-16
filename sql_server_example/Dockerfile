# base image slim configuration of python runtime
FROM continuumio/miniconda3

# install msodbcsql
RUN apt-get update && apt-get install -y curl && apt-get install -y gnupg2

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/8/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN exit && apt-get update && ACCEPT_EULA=Y apt-get install msodbcsql17
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"
RUN apt-get install -y unixodbc-dev

# establish the working directory
WORKDIR /app
ADD environment.yml /app

# create environment and set the python interpreter
RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/docker_tutorial/bin:$PATH

# expose port to the outside world
EXPOSE 8080

# add source code
ADD . /app

# run app.y
CMD ["python", "app.py"]