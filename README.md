# Ad Filtering Proxy Service

## Table of Contents

- [Client requirements](#client-requirements)
- [Technologies](#technologies)
- [How to run application](#how-to-run-application)
- [Testing the API endpoint](#testing-the-api-endpoint)
- [Project Status](#project-status)

## Client requirements

As part of a large piece of work, the Advertising Technology team needs to develop a Filtering Proxy service to support Advertising Decisioning on a brand new service.

This task is to build a RESTful service which determines if a targeted advert should be requested, or that the linear advert should be shown without a substitution.

The service endpoint receives the following in the request parameters :

- _customerId_ - numeric - 12 digit ID for the Customer the service is registered to
- _optIn_ - True/False - indicating if the Customer has opted in to targeted advertising
- _inactivityTimer_ - numeric - number of seconds since the Customer last used the remote

> ### Deliverable

API will return relevant response codes (200/4xx/5XX) with response {‘value’ : True/False} based on the following logic:

- 🚀 If `optIn` is False, they have not given permission to send targeted adverts so you must return False
- 🚀 If `inactivityTimer` is greater than 2 hours then they have left the room, or fallen asleep, and so we do not send them any more targeted ads, so return False
- 🚀 If `customerId` is exactly divisible by 7 then they are part of the market segment the linear advert is aimed at and so we do not want them to get a targeted ad as the original ad is already targeting them, so return False.
- 🚀 If `inactivityTimer` is exactly divisible by 9 then the downstream ad decision system is offline, so return False
- 🚀 Otherwise return True

> ### Application notes

- I choose to use Postgres for the database for this project. My reasoning to use Postgres was that it is a more secure database than SQLite, and as we are storing data from customers that is sensitive and private, this data needs to be secure and safe.

- For this project I did not use any git versioning control system, but if I was to use git, this would be saved to a github repo, with any changes to be added being done in specific branches. These would then be approved and merged to the main/master branch.

## Technologies

- Python - [Python 3.11](https://www.python.org/)
- Django 4.1
- Django Rest framework
- Swagger Docs
- PostgreSQL
- pytest

## How to run application

- [Virtual Environment](#virtual-environment)
- [Dependencies](#dependencies)
- [Setting up environment variables](#setting-up-environment-variables)
- [Setting up PostgreSQL](#setting-up-postgresql)
- [Migrate models to database](#migrate-models-to-database)
- [Export data from customers file to database](#export-data-from-customers-file-to-database)
- [Django Admin](#django-admin)
- [Launch Django Admin Site](#launch-django-admin-site)
- [Pytest](#pytest)
- [Troubleshooting](#troubleshooting)

### **_Virtual Environment_**

> It's good practice to work on a virtual environment with it's own dependencies and packages.

1 - To create a virtual environment on your machine follow the commands below:

```
$ python -m venv venv
```

2 - Activate the newly created environment:

```
$ source venv/bin/activate
```

You should see the env_name on your terminal as shown in the example below.

```
(venv) computer:~/projects/$
```

### **_Dependencies_**

> To install all dependencies saved in the requirements.txt file in your virtual environment run the command below:

```
$ pip install -r requirements.txt
```

> After installing dependencies run the code below to make sure the app is using dependencies installed in virtual environment.

```
$ deactivate && source venv/bin/activate
```

### **_Setting up environment variables_**

> We want to keep our sensitive data safe, so we use the .env file to store all our sensitive data in environment variables.

- Make a copy of the .env.template file and save it as `.env` in the same directory as the manage.py file.
- The file already has Environment variables in it, they just need to be populated as shown below.

```
SECRET_KEY='< Generate a new SECRET_KEY with `python manage.py generate_secret_key`  >'
DB_NAME='< database name >'
DB_USER='< database user name>'
DB_USER_PASSWORD='< database password >'
DB_HOST='< localhost or 127.0.0.1 >'
DB_PORT='< 5432 >'
```

- Save the `.env` file and that's it.

### **_Setting up PostgreSQL_**

This application uses PostgreSQL for the database, for us to run the application we first need to set up PostgreSQL with the relevant database for this project.  
Please follow the [Set up PostgreSQL](/documentation/set_up_postgresql.md#instructions-to-set-up-postgresql) instructions.

### **_Migrate models to database_**

> In order to add data to our database we need to create some tables to store this data, follow the commands below to create tables from our models.

- Create the tables from the available models

```
$ python manage.py makemigrations
```

- Migrate tables to database

```
$ python manage.py migrate
```

> **Note:** Every time you change something in any of the models file, both commands above need to be run in order for the changes to be reflected in the database tables.

### **_Export data from customers file to database_**

> Now that we have PostgreSQL set up and ready, use the command below to add some customers data to the database.

```
$ python manage.py extract_data_from customersList.json
```

### **_Django Admin_**

> To be able to interact with the django admin site, you need to have a user log in, use the command below to create a django superuser.  
> This will ask you for a username, email and password.

```
$ python manage.py createsuperuser
```

### **_Launch Django Admin Site_**

> Use the command below to start the django application server

```
$ python manage.py runserver
```

### Navigate to [Django Admin](http://127.0.0.1:8000/admin) and have fun. 🚀

> Here you can double check that the data has been populated into the database.

### **_Pytest_**

> Run the following command in your command line to run all the tests in the project:

```
$ pytest
```

> If you'd like to see more details of what is being tested, run the command below:

```
$ pytest -v
```

### **_Troubleshooting_**

> _dotenv_  
> If after installing dependencies from requirement.txt, `dotenv` import in the settings file doesn't get recognized, try to restart you IDE code editor.

### **_Testing the API endpoint_**

### You can test the API endpoint in two different ways:

> With Django Server running, use the swagger link below, and test the available parameters with different values.

[Swagger Docs](http://127.0.0.1:8000/swagger/)

```
http://127.0.0.1:8000/swagger/
```

> Or follow the links below and see the returned values.

- Returns `False` as `optIn` is set to false

```
http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000002&optIn=False&inactivityTimer=7000
```

[Link](http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000002&optIn=False&inactivityTimer=7000)

- Returns `False` as `inactivityTimer` is greater than 2 hours

```
http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000002&optIn=True&inactivityTimer=7500
```

[Link](http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000002&optIn=True&inactivityTimer=7500)

- Returns `False` as `customerId` is exactly divisible by 7

```
http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000014&optIn=True&inactivityTimer=750
```

[Link](http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000014&optIn=True&inactivityTimer=750)

- Returns `False` as `inactivityTimer` is exactly divisible by 9

```
http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000003&optIn=True&inactivityTimer=18
```

[Link](http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000003&optIn=True&inactivityTimer=18)

- Returns `True` as all the conditions evaluate to true

```
http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000002&optIn=True&inactivityTimer=7000
```

[Link](http://127.0.0.1:8000/request-targeted-ad/?customerId=000000000002&optIn=True&inactivityTimer=7000)

> Alternatively you can also edit these parameters in your browser url.

## Project Status

> To Do's

> Done

- ✅ Remove print statements from customer_data_handler

_Swagger Documentation_

- ✅ Add swagger docs

_API endpoint_

- ✅ Create ad filtering proxy app
- ✅ Create serializers to serialize required data from models
- ✅ Add endpoint to views and urls files
- ✅ Work on logic to return values according to [Deliverable](#deliverable)
- ✅ Address invalid inputs errors

_Data to populate database_

- ✅ Create json file with dummy data
- ✅ Create command management to extract data and load to DB

_Creating Models_

- ✅ Create models for database tables to store:
  - ✅ Customer IDs
  - ✅ Customer details
  - ✅ Customer password
- ✅ Add models to the `init` file in models
- ✅ Create Factories for testing models
- ✅ Create tests for models
- ✅ makemigrations
- ✅ migrate

_Setting up_

- ✅ Create database in Postgresq `customersdb`
- ✅ Create project dir
- ✅ Set up virtual env
- ✅ pip install Django
- ✅ pip install psycopg2
- ✅ pip install pytest
- ✅ pip install python-dotenv
- ✅ pip freeze > requirements.txt
- ✅ Create django project
- ✅ Create django app
- ✅ Add README file to project
- ✅ Add documentation dir with Postgresql instruction file
- ✅ Create .gitignore file
- ✅ Add .env.template file for PostgreSQL credentials
- ✅ Add .env file and set up config/settings.py for PostgreSQL
