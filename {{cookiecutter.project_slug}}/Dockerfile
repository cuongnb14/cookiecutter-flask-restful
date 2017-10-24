# Author: {{cookiecutter.author_name}}
#
# Build: docker build -t {{cookiecutter.project_slug}}:{{cookiecutter.version}} .
# Run: docker run -d -p 5000:5000 --name {{cookiecutter.project_slug}} {{cookiecutter.project_slug}}:{{cookiecutter.version}}
#-----------------------------------------------------------------------------------------------------------------------

FROM ubuntu:16.04
MAINTAINER {{cookiecutter.author_name}} {{cookiecutter.email}}

RUN apt-get update -qq

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip build-essential python3-dev

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libmysqlclient-dev libxml2-dev libxslt1-dev libssl-dev libffi-dev locales

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install -r requirements.txt

RUN pip3 install honcho

EXPOSE 5000

ENV C_FORCE_ROOT="true"
CMD ["honcho", "start"]