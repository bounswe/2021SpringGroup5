<h1> Random Activity Generator API </h1>
<h2>Brief explanation of the API</h2>
<p>Random activity generator API is an application programming interface which shows different activities every time it asked. It generates different types of activities with different number of people.
Target user of the API is bored people as it is written at the top of the html page. For generating random activities, as a third party API, boredAPI (https://www.boredapi.com/) is used.</p>

<h2>Request and response of boredAPI</h2>
<p>It requests with get method via http://www.boredapi.com/api/activity/.</p>
<p>Result of this request is in JSON format. An example output is like that:</p>
<p>
  {
</p>
<p>
	"activity": "Learn Express.js",</p>
<p>
	"accessibility": 0.25,</p>
<p>
	"type": "education",</p>
<p>
	"participants": 1,</p>
<p>
	"price": 0.1,</p>
<p>
	"link": "https://expressjs.com/",</p>
<p>
	"key": "3943506"</p>
<p>
} 
</p>

<h2>Used Tech</h2>
<p>In the process of producing the API, Django and Django Rest Framework are used. So we used python. </p>
<p>Other than backend usage, HTML is used to show output of the API.</p>
<p>As database it is decided to use PostgreSQL. For the entire project of practise-API we used PostgreSQL as a team. </p>

<h2>Function</h2>
<h3>def showActivity(request)</h3>
<p>This function communicate with the other API. It requests Get from http://www.boredapi.com/api/activity/. And in return renders the input as activity, type, and participants. It returns JSON response as an
  output.</p>
  
  
<h2>User Interface of the API</h2>
![randomActivity](https://user-images.githubusercontent.com/81261090/121298659-e8530200-c8fc-11eb-92d4-a0a95fcaf8da.png)


  

