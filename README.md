
CREATING A DOCKERISED APPLICATION

## Description

This is a simple web application that displays the message "Hello, Welcome to KodeCamp DevOps Bootcamp!". The application is built using Python and Flask, containerized using Docker, and deployed to a Kubernetes cluster.

## Steps

1. **Create the application:**
   - Created a Python Flask application that displays the message.

2. **Dockerize the application:**
   - Wrote a Dockerfile to containerize the application.
   - Built and ran the Docker image locally.
   - Tagged and pushed the Docker image to Docker Hub.

3. **Deploy to Kubernetes:**
   - Created Kubernetes manifest files for Deployment and Service.
   - Deployed the application to a Minikube cluster.
   - Port-forwarded the service and accessed the application in a web browser.

## Docker Image URL

[Docker Hub - myapp](https://hub.docker.com/r/yasinymg/myapp)

## Issues Encountered

- Issue 1: I had an issue with defining ports, i went through the docs and managed it.
  
- Issue 2: port fowarding was an issue too 
  

## Screenshots

- **Application Running:**
  ![Application Screenshot](screenshots/application-running.png)

-**kubernetes Pods:**
![Kubernetes Pods](screenshots/kubernetes-pods.png)

-**kubernetes Services:**
![Kubernetes services](screenshots/kubernetes-dervices.png)



