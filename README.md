[![CircleCI](https://dl.circleci.com/status-badge/img/gh/buklawz/operationalize-machine-learning-microservice-api/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/buklawz/operationalize-machine-learning-microservice-api/tree/main)

## Project Overview

The project entails operationalizing a python flask app—in a provided file, `app.py`—that serves out predictions (inference) about housing prices through API calls. 
The primary aim of the project is to containerize the python flask-app and deploy the container in Kubernetes cluster. 

### Project Tasks

* Test project code using linting
* Complete a Dockerfile to containerize this application
* Deploy containerized application using Docker to Dockerhub 
* Make a prediction by running the `make_prediction.sh` script
* Improve the log statements in the source code for the application
* Configure Kubernetes and create a Kubernetes cluster
* Pull the image from Dockerhub and deploy to local Kubernetes cluster
* Make a prediction by runiing the `make_prediction.sh` script
* Run circleci workflow

---

## Setup the Environment

* Create a virtualenv and activate it

```
python3 -m venv <your_venv>
source <your_venv>/bin/activate
```

* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh`

### Kubernetes Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
* Create Flask app in Container
* Run using kubectl

### Files

* `output_txt_files/docker_out.txt` contains logs returned after running the app with Docker
* `output_txt_files/kubernetes_out.txt` containes logs and the prediction returned after running the app with Kubernetes(`run_kubernetes.sh`)
* `run_docker.sh` contains the steps to get Docker running the app locally
* `run_kubernetes.sh` contains the steps to get Kubernetes running the app locally
* `upload_docker.sh` contains the steps to upload the image to the Docker repository
*  `Screehshots ` of the different steps of executing the project are also included.
