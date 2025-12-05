## Dockerized Python Application with PostgreSQL Integration

## Project Objective
The objective of this project was to containerize a Python application that interfaces with a PostgreSQL database. The project demonstrates the use of Docker for application deployment, network management, and data persistence.

## Tools & Technologies Used
Docker Desktop: For container management.
Python 3.10: Application logic.
PostgreSQL: Relational database.
VS Code: Integrated Development Environment.

## Prerequisites
Ensuring Docker Desktop is installed and running.

## Creating the Files
## create the Python App
Creating a new file named app.py.
## Creating the Dockerfile.
Creating a new file named Dockerfile with no extension.
 
## Runing the app
## Creating a Network
This allows your app to talk to the database.
Command:- docker network create mynetwork

## Starting the Database
This runs a PostgreSQL database in the background.
Command :- docker run -d --name my-postgres --network mynetwork -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=user -e POSTGRES_DB=mydb postgres

## Building App
This packages my Python file into a "Docker Image".
Command :- docker build -t my-python-app .
 
## Running my App
This runs my app and connects it to the database.
Command :-  docker run --rm --network mynetwork my-python-app

This proves that your Python app connected to the Database, inserted data, and read it back successfully.

## Pushing to Docker Hub
## Login
Command :- docker login
 
## Tagging my Image
Re-tagging my image with my Docker Hub username.
command :- docker tag my-python-app <akarshkoppolu14>/my-python-app

## Pushing to Docker hub
command :-  docker push akarshkoppolu14/my-python-app


## Cleanup
commands to clean up:-
1.	docker stop my-postgres
2.	docker rm my-postgres
3.	docker network rm mynetwork
4.	docker rmi my-python-app
 



