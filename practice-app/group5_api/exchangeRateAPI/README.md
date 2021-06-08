# Exchange Rate API

Hello and Welcome to my API.

My API is written in Python and Django.

The main goal of the API that learn GET, POST methods and database operations like insert or select.

In the API, you can add category, get category by name, get all categories, add event post, get unique event post by post id, get all event posts.
In addition to these, the API is also connected to another API which is Open Exchange Rates API which provides all currencies rates based on USD continuously.
You can see 1 USD how much others currencies like TRY, CNY, RUB
Also, you can convert to any amount USD to others currencies. For example, 100 USD convert to TRY.

You can access to all feates from main link which is http://127.0.0.1:8000/exchangeRateAPI/

### How to run the app:

- Clone the repository
- Create and activate a virtual environment
- Install the requirements
- Run the following command to create the tables in the database:

`python3 ./manage.py migrate`

- Run the following command to start the app:

`python3 ./manage.py runserver`

- Open the browser (http://127.0.0.1:8000/exchangeRateAPI/)
- Quit the app using ctrl+c
- You can test the app using the following command:

`python3 ./manage.py test`


For more info please contact [me](https://github.com/umutgun17).
