
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
  

## For the UI of the API

This is a stub UI for the API.
### GET /airQuality/?lat={{LATITUDE}}&lon={{LONGITUDE}}

### GET /airQuality/?user_id={{USER_ID}}
This calls GET methods from /airQuality/api/pollution with according arguments and shows the result on a basic template.
