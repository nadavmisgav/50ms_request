# The Case of the 50ms request

This repo is a live demo of the puzzle `The Case of the 50ms request` from [wizardzines's mysteries](https://mysteries.wizardzines.com/), thus allowing for people to investigate the problem and try to debug it themselves.

## Getting started

### Compose container

Build the docker images and run them

```bash
docker-compose up
```

You will see the logs generated by the containers.

### Interactive shell

Run an interactive shell inside either container for investigating

```bash
docker exec -it server /bin/sh # For server
docker exec -it client /bin/sh # For client
```

> Notice that the hostname of both containers are server/client respectively.

### Server

The server runs a simple [python server](server/server.py) that listens on port `8000`

> IMPORTANT: Do not look at the server implementation (`server.py`) it contains spoilers.

### Client

The client is just a simple alpine based image containing a script [slow.js](client/slow.js)
that recrates the problem, by posting data to the server and measuring the time it took.

```bash
node slow.js
```

You are allowed to examine this script.

## Solution

The solution can be found [here](SOLUTION.md).
