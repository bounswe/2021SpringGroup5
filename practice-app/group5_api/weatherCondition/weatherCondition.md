# weatherCondition API description

## Endpoint
```http://localhost:8000/weatherCondition/api```

## GET functionality
It returns an empty json with status code 200.

## POST functionality
When the user gives a json in this format:
```{ Town : town_name }```
it returns the weather condition of the town with the data of the previous search.

## Functions
### def weather_api(request)
It returns json response for the get and post requests. If the request is a GET, then ```weather(method,searchTown=None)``` is called with the parameter request.method which is "GET" and not any town information is sent to the method ```weather(method,searchTown=None)``` since this is a GET request. <br>
If the request is POST, then ```weather(method,searchTown=None)``` is called with the parameter request.method which is "POST" and request.POST.get("Town") which is the given town name to search the weather condition.<br>
```weather(method,searchTown=None)``` returns json response for both type of requests and these responses are also returned by the ```def weather_api(request)``` function.

### def weather(method,searchTown=None)

method: Stores the type of the request<br>
searchTown: Stores the searched town name for POST requests. It is None if the request type is GET.<br>

For method==GET: <br>
Return value: ```Response({},status=status.HTTP_200_OK) ```<br>

For method==POST:<br>

Weather condition of a town is returned from openweathermap API via this URI:<br>
```http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric``` <br>

Return value:
Data of the previous search is also provided. If openweathermap API returns with status code 200, the validity of the data is
checked. If the data fits the limits of the model then the data is saved in the database, old and new weather conditions are
returned with the status code 201. If the data doesn't fit the limits of the model, then only the previous data ise sent with the status code 400. <br>


### API key
It can be found in the .env file of the group5_api folder.<br>