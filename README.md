## Rolltime Collect
Collector for CitiBike's public data. It runs on a highly redundant schedule (4 x per minute) on multiple nodes. Stores data to the same database (`postgres`) to make sure no data-point goes missing.

[![Build Status](https://travis-ci.org/rolltime/rolltime-collect.svg?branch=master)](https://travis-ci.org/rolltime/rolltime-collect)


## Setup and Run
To build, test, and run the application locally, run:

```
$ make setup
$ make test
$ make run
```


## Docker Setup
[![](https://badge.imagelayers.io/luiscape/rolltime-collect:latest.svg)](https://imagelayers.io/?images=luiscape/rolltime-collect:latest 'Get your own badge on imagelayers.io')

This collector is designed to run on a Docker container. Please refer to the `Dockerfile` for the inner-workings of the application. The container must be run with no local volumes, but with a link to a `PosgreSQL` container.

```shell
$ docker run \
  -d
  --name collector \
  --link node_watch:node_watch \
  --link postgres:postgres \
  -e NODE_ID=collector-newyork-01 \
  rolltime/rolltime-collect:latest
```
