# Daily Quote API

Welcome to the Daily Quote API.

The Daily Quote API is an API that provides you daily quotes about sports, in English. 
It uses the [Quotes Rest API](https://quotes.rest/) as the remote API. 
The remote API provides a different quote for each date (quote of the day functionality). 
The Daily Quote API filters the quote category as sports and the quote language as english
by making a get request to 'https://quotes.rest/qod?category=sports&language=en'

The API is written in Django and is connected with a PostgreSQL database.
The Daily Quote API is a RESTful API.
Each day's quote, author and date is saved to the database if it has not been saved before.

The Daily Quote API adds a rating functionality to the remote API.
It supports GET and POST methods.

When a user makes a GET request to the API, 
they see the average rating of the quote and the number of ratings made so far,
along with the quote and the author.

Users can rate the quote with a point of their wish. Allowed points are 0,1,2,3,4 and 5.
When a POST request is made with a valid point,
the total points of the quote is incremented by the given point
and the total ratings of the quote is incremented by one.
These values are updated in the database.
Then, the new average value and number of ratings are returned in the response.

The front-end is implemented using HTML. 
The HTML forms allows the API to get only valid inputs when taking a POST request.

Unit tests are provided for the API.
The details of the tests and functionality they test are explained in the comments.

The functionality can be seen in the screenshots:

<img width="700" src="https://user-images.githubusercontent.com/48058901/120921281-a68f4500-c6cb-11eb-88a9-6edaacf0690b.png">

<img width="700" src="https://user-images.githubusercontent.com/48058901/120921283-a8f19f00-c6cb-11eb-816d-6ebeeaf1f442.png">

<img width="700" src="https://user-images.githubusercontent.com/48058901/120921284-aa22cc00-c6cb-11eb-94a9-7c8123a7cee4.png">

### How to run the app:

- Clone the repository
- Create and activate a virtual environment
- Install the requirements
- Set up a postgresql database named group5db
- Run the following command to create the tables in the database:

`python3 ./manage.py migrate`

- Run the following command to start the app:

`python3 ./manage.py sunserver`

- Open the browser (http://127.0.0.1:8000/)
- Enjoy the app
- Quit the app using ctrl+c
- You can test the app using the following command:

`python3 ./manage.py test`


For more info please contact [me](https://github.com/zudiay).
