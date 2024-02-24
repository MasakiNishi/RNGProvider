# RNGProvider Microservice

## Overview
This document provides instructions on how to interact programmatically with the RNGProvider microservice, a Django-based application designed for generating random numbers within a specified range.

## Prerequisites
Before you begin, ensure you have the following installed:
- [Visual Studio Code](https://code.visualstudio.com/) with the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
- [Docker](https://www.docker.com/) for creating and managing the application's container.

## Setup Instructions

### Starting the Development Environment
1. Clone the project repository to your local machine.
2. Open the project in Visual Studio Code.
3. Use the `Remote-Containers: Open Folder in Container` command from the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) to start the containerized development environment.

### Running the Django Server
Inside the container, start the Django application using the following command:
```bash
python manage.py runserver --settings=config.settings.development
```
This command will start the Django development server, making the application accessible through `http://localhost:8000/`.

## Interacting with the Microservice

### Making a Request
To request a random number, make a GET request to the `/api/rng/provider/` endpoint. You can specify the `min` and `max` values for the random number generation using query parameters.

**Example Request:**
http://localhost:8000/api/rng/provider/?min=10&max=200

If `min` and `max` are not specified, default values are used (`min=0` and `max=10000`).

### Receiving a Response
The service will respond with a JSON object containing the generated random number.

**Example Response:**
```json
{
    "random_number": 152
}
```
The response will have a status code of HTTP 200 OK, indicating a successful request.

## UML diagram
![UMLSequence](https://github.com/MasakiNishi/RNGProvider/assets/23161699/4e8a99ab-cddc-48e7-aab8-a29fdae31e07)
