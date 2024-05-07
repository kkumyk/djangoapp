## Project Setup with [Poetry](https://python-poetry.org/docs/cli)

1. [create a new poetry project](https://realpython.com/dependency-management-python-poetry/#create-a-new-poetry-project);
2. Create [virtual env](https://medium.com/@AgnesMbiti/creating-a-python-virtual-environment-on-ubuntu-22-04-5efc173ce655) and activate it;
3. use <i>[poetry add](https://realpython.com/dependency-management-python-poetry\/#declare-runtime-dependencies)</i> django, asgiref and sqlparse command to add django latest version to the pyproject.toml file; this command does also installs django in the virtual env;

<hr>

### Side Notes

- <i>pyproject.toml</i> lists all the project dependencies;

- <i>poetry.lock</i> keeps all the project dependencies constant so that if other people want to use your project, they will be able to install the exact same versions;

- see also [Setting up a basic Django project with Poetry](https://builtwithdjango.com/blog/basic-django-setup)

## Initiate a Django project
- Return to the terminal. In the terminal, create a Django project called my_project in the current directory.

- <i>poetry run</i> runs the django-admin command for me from the virtual environment that will have all the dependencies that we specified earlier
- Remember that the shortcut to refer to the current directory is a single dot . at the end of the command.

Initiate a Django project with the Django admin command: 
> poetry run django-admin startproject my_project .

-  Return to the terminal and start the Django server with the following command:
> poetry run python3 manage.py runserver

- Open your browser and see a bare-bones Django project.

## Creating a Django app

- Now we have a Django project created, we need to make an app. To do this, we use the manage.py file. In the terminal, type:
> poetry run python3 manage.py startapp hello_world
- Note: Check the explorer panel to see the new hello_world app directory has been created.

## Creating Views

- In hello_world/views.py, below from django.shortcuts import render, type:
> from django.http import HttpResponse
- add a Python function named index. Inside the function, we are returning a simple HTTP response.

## Adding our app to the settings.py file

- To connect the app you will need to scroll down through the my_project/settings.py file to find the INSTALLED_APPS list.

## Test your app
> poetry run python3 manage.py runserver
