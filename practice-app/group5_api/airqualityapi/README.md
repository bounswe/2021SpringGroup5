
  

# AirQuality API description

  

This is a simple API which returns air quality index and corresponding risk category for a specified location. If provided with a user_id it can store locations for a user and later use them to return air quality data.

  

This API uses [IQ Air AirVisual API](https://www.iqair.com/air-pollution-data-api) to get air quality index data.

  

## API Routes

For air pollution services:

/airQuality/api/pollution/

For location history services:

/airQuality/api/location/

  

## API functionality

  

### GET /airQuality/api/pollution/?lat={{LATITUDE}}&lon={{LONGITUDE}}

  

Returns air quality, classification of air quality, description, city and country of given coordinates.

  

Arguments:

- lat: Latitude of the coordinate

- lon: Longitude of the coordinate

  

It returns a json.

  

### GET /airQuality/api/pollution/?user_id={{USER_ID}}

  

Returns air quality, classification of air quality, description, city and country; based on latest recorded location of the user with user_id

  

Arguments:

- user_id: Id of the user

  

It returns a json.

  

### GET /airQuality/api/location/

  

Returns all saved locations for all users, sorted by date added.

  

It returns a json.

  

### GET /airQuality/api/location/?user_id={{USER_ID}}

  

Returns all saved locations for a user, sorted by date added.

  

Arguments:

- user_id: Id of the user

  

It returns a json.

  

### POST /airQuality/api/location/

  

When the user gives a json in this format:

  

```{'user_id': '5', 'latitude': '39.7667', 'longitude': '30.5256'}```

  

It saves the coordinates and user_id.

  

## UI of the API

  

This is a stub UI for the API. It can be accessed from /airQuality

### GET /airQuality/?lat={{LATITUDE}}&lon={{LONGITUDE}}

  

### GET /airQuality/?user_id={{USER_ID}}

This calls GET methods from /airQuality/api/pollution with according arguments and shows the result on a basic template.

I didn't have much time creating an interface and this only uses get methods, it can be improved by adding some basic buttons. It can be accessed from this address: [http://3.127.142.97:8000/airQuality/](http://3.127.142.97:8000/airQuality/)
I am providing more input and outputs below.

## Input and Output
### POST /airQuality/api/locations/
Create a location for user id 61
Using data below:
```
{
	"user_id": 61,
	"latitude": 41.0027,
	"longitude": 39.7168
}
```
Output:
```
{
	"created": "2021-06-09T22:08:46.766111Z",
	"user_id": 61,
	"latitude": 41.0027,
	"longitude": 39.7168
}
```
---
### GET /airQuality/api/locations/?user_id=61
Get saved location of user id 61
Output:
```
[
	{
		"created": "2021-06-09T22:08:46.766111Z",
		"user_id": 61,
		"latitude": 41.0027,
		"longitude": 39.7168
	}
]
```
---
### GET /airQuality/api/pollution/?user_id=61
Find pollution on user's latest recorded location
Output:
```
{
    "aqi": 69,
    "name": "Moderate",
    "color": "#faff29",
    "description": "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.",
    "polluiton_ts": "2021-06-09T22:00:00.000Z",
    "city": "Trabzon",
    "state": "Trabzon",
    "country": "Turkey",
    "coordinates": [
        39.731671906746335,
        41.00458548106175
    ]
}
```
---
### GET /airQuality/api/pollution/?lat=39.7667&lon=30.5256
Get pollution of a location directly
Output:
```
{
    "aqi": 48,
    "name": "Good",
    "color": "#47e60e",
    "description": "Air quality is satisfactory, and air pollution poses little or no risk.",
    "polluiton_ts": "2021-06-09T22:00:00.000Z",
    "city": "Odunpazari",
    "state": "Eskisehir",
    "country": "Turkey",
    "coordinates": [
        30.53538,
        39.76821
    ]
}
```