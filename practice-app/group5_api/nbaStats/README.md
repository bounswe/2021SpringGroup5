# nbaStats API Description

   Welcome to nbaStats API.
You can search for NBA players by their name (and/or surname) and you can get some information about them.
API is developed with Django Framework. Also API uses 3rd party API [balldontlie].(https://www.balldontlie.io/api/v1/players)

API supports GET and POST methods. Frontend is implemented using HTML. HTML files are located in templates file.
Also API is provided tests. Command in order to run the tests:

    python manage.py test nbaStats

 
### Screenshots of Interface:

![html_interface1](https://user-images.githubusercontent.com/56520923/121224294-16026180-c891-11eb-8894-fb824f29b5ff.jpg)


![html_interface2](https://user-images.githubusercontent.com/56520923/121224507-4ea23b00-c891-11eb-9c50-61446e437704.jpg)



![html_interface3](https://user-images.githubusercontent.com/56520923/121224694-7ee9d980-c891-11eb-8e7c-b744a65d510b.jpg)




### How to run the app:

 - Clone the repository
 - Install the requirements
 - Set up a PostgreSQL database named `group5db`
 - Run the following command to create the tables in the database:

   `python3 ./manage.py migrate`

 - Run the following command to start the app:
  `python3 ./manage.py sunserver`

- Open the browser ([http://127.0.0.1:8000/](http://127.0.0.1:8000/)).

- Quit the app using Ctrl+C

You can run the tests with following command:

    python3 ./manage.py test

