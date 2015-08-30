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
  && cd rolltime-collect

WORKDIR "/rolltime-collect"

RUN make setup

CMD ["make", "configure", "&&", "make", "run"]
