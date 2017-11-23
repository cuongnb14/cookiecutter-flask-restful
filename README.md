# cookiecutter-flask-restful

Cookiecutter Flask-RESTful is a framework for jumpstarting production-ready Flask-RESTful projects quickly.

## Introduction
This cookie cutter is a very simple boilerplate for starting a REST api using Flask, Flask-RESTful, Celery. It comes with basic project structure and configuration, celery task.

**Features:**

- Simple flask-RESTful application
- Flask command line interface integration
- Implementation simple cli: init database, list all router
- Integrate celery for handle long process
- Simple pagination utils  
- Configuration using environment variable
- Dockerizer
- Use Makefile to install

**Used packages:**
- [Flask](http://flask.pocoo.org/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [mysqlclient](https://github.com/PyMySQL/mysqlclient-python)
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
- [Celery](http://www.celeryproject.org/)
- [gunicorn](http://gunicorn.org/)


## Usage

Step 1: Init project
 
`cookiecutter https://github.com/cuongnb14/cookiecutter-flask-restful.git`

Step 2: Install requirements

`make install-requirements`

Step 3: Build docker images

`make build`

Step 4: Run mysql container

`docker-compose up -d mysql`

Step 5: Init database schema

`make init-db`

Step 6: Run project

    - Without docker: `make run`
    
    - With docker: `make up`
    
 