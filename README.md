# reborn2020

TODO project doc here


## Prerequisites

* Python 3.6+ (or use the PyEnv)
* The requirements.txt installed
* Docker 
    * macOS: `brew install docker`
    * Windows: `choco install docker` (I think)
    * or follow the install guide from the docker website.

# Quick guide

Here the quick guide to running in docker.

* When not running yet...
Build and run the application in docker-compose:

```bash
docker-compose build reborn2020
docker-compose up -d
```

* Rebuild when already running:

```bash
docker-compose build reborn2020
docker-compose stop reborn2020 
docker-compose start reborn2020
```

* Stopping everything:

```bash
docker-compose stop
```

* Resetting everything:

```bash
docker-compose down -v
```

# The more complete guide

## Build Docker image

A docker image can be build from the application.

```bash
docker build -t reborn2020 .
```

or with docker-compose

```bash
docker-compose build reborn2020
```

## Run

to run the application you need two things to run: 
* The database and the wrapping application in this project

### Run the application

From the root of the project:

To start the database:
```bash
docker-compose up [-d]
```
the -d will run it in daemon or detached mode (as background process)

To stop the database:
```bash
docker-compose stop
```

To reset the database completely:
```bash
docker-compose down -v
```

### Run Application (standalone)

```bash
python3 main.py
```

You might have to stop the build app in docker compose first.

```bash
docker-compose stop reborn2020
```

# Extra tools

## HTTP Client 

In the root of the project you will find a file called `client.http`.
If you use IntelliJ or equivalent IDE from Jetbrains you can use this file to run queries on 
application. A couple of example queries have been supplied.


## MongoDB interface

If you use the docker compose to run mongo you can find a GUI here:

* [MongoDB Express interface](http://localhost:8081)
