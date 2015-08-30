#######################################################
# Rolltime collector. Designed to run on many nodes at
# the same time. Connects to a PostgreSQL container
#######################################################

FROM python:2.7.10

MAINTAINER Luis Capelo <luiscape@gmail.com>


#
# Clone app from GitHub
# and install dependencies.
#
RUN \
  git clone https://github.com/rolltime/rolltime-collect \
  && cd rolltime-collect \
  && make setup

#
# Making sure terminal
# uses utf-8.
#
RUN \
  export LC_ALL=en_US.UTF-8 \
  && export LANG=en_US.UTF-8 \
  && export LANGUAGE=en_US.UTF-8

WORKDIR "/rolltime-collect"

CMD ["make", "configure", "&&", "make", "run"]


docker run \
  -d \
  --name collector \
  --link postgres:postgres \
  -e HOST_DATABASE='1.1.1.1' \
  test/test:test
