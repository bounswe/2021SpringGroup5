## Frontend

The deployment part is easy for a React app. It is as follow:

1. Go to frontend app path:  `cd project/frontend/app`
2. Build the app to static components: `npm run-script build`
3. Deploy the built application to Amazon S3 : `npm run-script deploy` which runs the command written by us innerly. Alternatively, you can directly run the command `aws s3 sync build/ s3://cmpe451-frontend`
