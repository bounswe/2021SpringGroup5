## Frontend

The deployment part is easy for a React app. It is as follow:

1. Go to frontend app path:  `cd project/frontend/app`
2. Build the app to static components: `npm run-script build`
3. Deploy the built application to Amazon S3 : `npm run-script deploy` which runs the command written by us innerly. Alternatively, you can directly run the command `aws s3 sync build/ s3://cmpe451-frontend`


## Android

# Installation
You can use your Android device or an emulator in order to use Ludo Mobile Application.

- With .apk file 
Latest version of .apk file can be found here:[latest .apk version](https://github.com/bounswe/2021SpringGroup5/blob/master/project/android/app/build/app/outputs/flutter-apk/app-release.apk)

# Features
* Sign-up
* Sign-in
* Forgot Password
* Create Event
* Search Event
* Filter Event
* Sort Events by Date
* Sort Events by Name
* Home Page
* Profile Page
* See Received Badges
* See Participated Events
* Log-out
