# cookiecutter-flask-restful

In development ...

## Usage

Step 1: Init project
 
`cookiecutter https://github.com/cuongnb14/cookiecutter-flask-restful.git`

Step 2: Install requirements

`make install-requirements`

Step 3: Run mysql container

`docker-compose up -d mysql`

Step 4: Init database schema

`make init-db`

Step 5: Run project without docker

`make run`
