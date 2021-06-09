# Authentication and Random Person API

Welcome to my Authentication and Random User API. This API is written in Django and Python.
The main goal of the API that learn GET, POST methods and database operations like insert or select.

In this API; you can add user, log in and log out and see how many registered users are there in that API and also
you can get a random person's name, gender and age.

You can access my API from main link : http://127.0.0.1:8000/authentication/

### How to run the app:
- Clone the repository
- Install the requirements
- Run the following command to create the tables in the database:

`python3 ./manage.py migrate`

- Run the following command to start the app:

`python3 ./manage.py runserver`

- Open the browser (http://127.0.0.1:8000/authentication/)
- Quit the app using ctrl+c
