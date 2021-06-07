Sport Relation API is an API to learn similarities between different sports and take a suggestion from API. 

API is developed with Django Framework, and it uses PostgreSQL DBMS. Also, It uses [Decathlon API](https://developers.decathlon.com/products/sports/docs).

There are three capabilities of API. 

1. You can fetch a detailed sport information with a sport `pk`
2. You can learn top 5 similar sports to a sport by giving a sport `pk`
3. You can get a suggestion from the API to learn which sport is the most relevant sport for you by giving three sports you interested in.

API has a user interface which developed with help of html templates rendering by Django. You can interact with API with help of UI.

### Screenshots of UI:

<img width="1436" alt="Screen_Shot_2021-06-08_at_01 20 31" src="https://user-images.githubusercontent.com/46852761/121095302-c6705700-c7f8-11eb-879e-244811458d63.png">
<img width="1436" alt="Screen_Shot_2021-06-08_at_01 20 54" src="https://user-images.githubusercontent.com/46852761/121095342-d720cd00-c7f8-11eb-8db4-922fecd5b9be.png">
<img width="1436" alt="Screen_Shot_2021-06-08_at_01 21 21" src="https://user-images.githubusercontent.com/46852761/121095395-f586c880-c7f8-11eb-8fc7-4b1387694652.png">

### **How to run the app:**

- Clone the repository
- Go to project folder
- Create and activate a virtual environment
- Install the requirements
- Set up a PostgreSQL database named `group5db`
- Run the command `python3 ./manage.py migrate` to create the tables in the database:
- Run the command `python3 ./manage.py sunserver` to start the app:
- Open the browser ([http://127.0.0.1:8000/](http://127.0.0.1:8000/))
- Get suggestions and learn similarities between sports!
- Quit the app using ctrl+c
- You can test the app using the command `python3 ./manage.py test`
