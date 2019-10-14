# base image slim configuration of python runtime
FROM continuumio/miniconda3

# establish the working directory
WORKDIR /app
ADD .. /app

# create environment and set the python interpreter
RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/docker_tutorial/bin:$PATH

# expose port 4000 to the outside world
EXPOSE 8080

# run app.y
CMD ["python", "app.py"]