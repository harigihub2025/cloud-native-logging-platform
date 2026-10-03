# Cloud-Native Centralized Logging Platform

A simple cloud-native application demonstrating containerization,
automated CI/CD, centralized logging, and service mesh concepts.

## Architecture

GitHub
   |
   v
AWS CodeBuild
   |
   v
Docker Build
   |
   v
Amazon ECR
   |
   v
Amazon ECS Fargate
   |
   v
AWS CloudWatch Logs

Local Kubernetes
   |
   v
Istio
   |
   v
Flask Application

## Technologies

- Python
- Flask
- Docker
- Git
- GitHub
- AWS ECR
- AWS ECS
- AWS Fargate
- AWS CloudWatch
- AWS CodeBuild
- IAM
- Networking
- Kubernetes
- Istio

## Application Endpoints

### Home

GET /

Returns application status.

### Health

GET /health

Returns application health status.

### Logs

GET /logs

Generates multiple application log messages.

### Error

GET /error

Generates an example error log.

## Run Locally

Install dependencies:

pip install -r requirements.txt

Run Flask:

python app.py

Application:

http://localhost:8080

## Docker

Build image:

docker build -t cloud-native-logging .

Run container:

docker run -p 8080:8080 cloud-native-logging

## AWS Architecture

The Docker image is stored in Amazon ECR and deployed
using Amazon ECS Fargate.

Container logs are sent to CloudWatch Logs using
the ECS awslogs log driver.

AWS CodeBuild automatically builds the Docker image
and pushes it to Amazon ECR.

## Logging Flow

Flask Application
        |
        v
Docker Container
        |
        v
ECS Fargate
        |
        v
CloudWatch Logs

## Project Objective

The objective of this project is to demonstrate a
cloud-native deployment and centralized logging workflow
using AWS managed services.