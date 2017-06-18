# Dillinger

eig-daredevils-user-microservice is a coordinating backend service. Two instances of this service will run, one each for Avengers and Xmen. It functions as the user management, authentication, authorization(JWT token), serve todos. The service also allows XMEN server to access AVENGERS todo with the correct digital signature and vice-versa. The service gives a redirect endpoint that logs the Avenger user to log in to Xmen server without re-entering the credentials.
    
  - User management 
  - Authentication
  - Authorization
  - Serve todos
  - Both instances(xmen and avenger) can access each others todo
  - Redirect to each others instance without re-entering the credentials

### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](http://breakdance.io) - HTML to Markdown converter
* [jQuery] - duh

### Installation

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ npm run predeploy
$ NODE_ENV=production node app
```


# eig-daredevils-user-microservice
user microservice


## create user

### request

#### by curl
```
curl -X POST \
  http://172.16.173.56:8000/user \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "data": {
    "username": "logan",
    "password": "12345678",
    "email":"test@g.com",
    "firstname": "feacdfdf",
    "lastname": "world",
    "superpower": "fire"
  }
}'
```

#### by AJAX
```
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://172.16.173.56:8000/user",
  "method": "POST",
  "headers": {
    "content-type": "application/json",
    "cache-control": "no-cache",
  },
  "processData": false,
  "data": "{\n\t\"data\": {\n\t\t\"username\": \"logan\",\n\t\t\"password\": \"12345678\",\n\t\t\"email\":\"test@g.com\",\n\t\t\"firstname\": \"feacdfdf\",\n\t\t\"lastname\": \"world\",\n\t\t\"superpower\": \"fire\"\n\t}\n}"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```
### response
success then, status 201
failure then, status 500

---------------------------------------------------------------------------------------------------------------------------------

## authenticate

### request
#### by curl
```
curl -X POST \
  http://127.0.0.1:8000/authenticate \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -d data=%7B%22username%22%3A%22spongebob%22%2C%22password%22%3A%22spongebob%22%7D
```

#### by ajax
```
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://127.0.0.1:8000/authenticate",
  "method": "POST",
  "headers": {
    "content-type": "application/x-www-form-urlencoded",
    "cache-control": "no-cache",
  },
  "data": {
    "data": "{\"username\":\"spongebob\",\"password\":\"spongebob\"}"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

### response
```
{ "username": "spongebob",
  "userid": 3,
  "accesstoken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywidGltZSI6MTQ5NzU5Mjc1N30.PJHqkaeMdi9Xpr5-z7GZtAI3oqZWr0lEBaq66CO5DUU"}
```

---------------------------------------------------------------------------------------------------------------------------------



## logout

### request

#### by curl
```
curl -X DELETE \
  http://127.0.0.1:8000/authenticate \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywidGltZSI6MTQ5NzU5NTc4N30.dNOfgARRjBtVyB9WJMgLSXyo5-JTwzp9eZU8-pu-4A4' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
```
#### by ajax
```
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://127.0.0.1:8000/authenticate",
  "method": "DELETE",
  "headers": {
    "accesstoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywidGltZSI6MTQ5NzU5NTc4N30.dNOfgARRjBtVyB9WJMgLSXyo5-JTwzp9eZU8-pu-4A4",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```
### response

success then, status 200
failure then, status 400


---------------------------------------------------------------------------------------------------------------------

## create todo

### by curl
```
curl -X POST \
  http://0.0.0.0:8000/todo \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywiZ3JvdXBpZCI6ImF2ZW5nZXIiLCJ0aW1lIjoxNDk3NjA4MDM0fQ.sqlu0uhtIFkg8sBRV_lzxpQPTOrvGWO7qL08Gfwaiwk' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "description" : "avenger group meet",
  "status" : "pending",
  "type" : "group"
}'
```
### by ajax
```
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://0.0.0.0:8000/todo",
  "method": "POST",
  "headers": {
    "content-type": "application/json",
    "accesstoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywiZ3JvdXBpZCI6ImF2ZW5nZXIiLCJ0aW1lIjoxNDk3NjA4MDM0fQ.sqlu0uhtIFkg8sBRV_lzxpQPTOrvGWO7qL08Gfwaiwk",
    "cache-control": "no-cache",
  },
  "processData": false,
  "data": "{\n\t\"description\" : \"avenger group meet\",\n\t\"status\" : \"pending\",\n\t\"type\" : \"group\"\n}"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```
--------------------------------------------------------------------------------------------------------------------

## dashboard

### by curl
```
curl -X GET \
  http://127.0.0.1:8000/dashboard \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywiZ3JvdXBpZCI6ImF2ZW5nZXIiLCJ0aW1lIjoxNDk3NjAwNzAyfQ.13p2p2naArvI8U_n8P9zy4osEN43QA5gIG5AQpW3VU0' \
  -H 'cache-control: no-cache' \
```
### by ajax
```
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://127.0.0.1:8000/dashboard",
  "method": "GET",
  "headers": {
    "accesstoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywiZ3JvdXBpZCI6ImF2ZW5nZXIiLCJ0aW1lIjoxNDk3NjAwNzAyfQ.13p2p2naArvI8U_n8P9zy4osEN43QA5gIG5AQpW3VU0",
    "cache-control": "no-cache",
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```


## Sanitize

```
curl -X POST \
  http://0.0.0.0:8888/sanitize \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imlyb25tYW4iLCJ1c2VyaWQiOjksImdyb3VwaWQiOiJhdmVuZ2VyIiwidGltZSI6MTQ5NzY0Mjc4OH0.7l1WWk4bz9AVs_WdijLlG4GXZvcTplB-7ocwh8wr4oo' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: c3075e3c-48a9-3ddc-94c1-f9cf9d2b0438' \
  -d '{
  "data": "<!DOCTYPE html>\r\n<html>\r\n<body>\r\n\r\n<div id=\"demo\">\r\n<h1>The XMLHttpRequest Object<\/h1>\r\n<button type=\"button\" onclick=\"loadDoc()\">Change Content<\/button>\r\n<\/div>\r\n\r\n<script>\r\nfunction loadDoc() {\r\n  var xhttp = new XMLHttpRequest();\r\n  xhttp.onreadystatechange = function() {\r\n    if (this.readyState == 4 && this.status == 200) {\r\n      document.getElementById(\"demo\").innerHTML =\r\n      this.responseText;\r\n    }\r\n  };\r\n  xhttp.open(\"GET\", \"ajax_info.txt\", true);\r\n  xhttp.send();\r\n}\r\n<\/script>\r\n\r\n\r\n<form action=\"\/action_page.php\">\r\n  <fieldset>\r\n    <legend>Personal information:<\/legend>\r\n    First name:<br>\r\n    <input type=\"text\" name=\"firstname\" value=\"Mickey\">\r\n    <br>\r\n    Last name:<br>\r\n    <input type=\"text\" name=\"lastname\" value=\"Mouse\">\r\n    <br><br>\r\n    <input type=\"submit\" value=\"Submit\">\r\n  <\/fieldset>\r\n<\/form>\r\n\r\n\r\n\r\n<a href=\"#\" onclick=\"$(this).next().fadeIn(); return false;\">Display my next sibling<\/a>\r\n\r\n<a href=\"#\" onclick=\"$(this).next().fadeIn(); return false;\">Display my next sibling<\/a>\r\n<a href=\"#\" onclick=\"$(this).next().fadeIn(); return false;\">Display my next sibling<\/a>\r\n<a href=\"#\" onclick=\"$(this).next().fadeIn(); return false;\">Display my next sibling<\/a>\r\n<a href=\"#\" onclick=\"$(this).next().fadeIn(); return false;\">Display my next sibling<\/a>\r\n\r\n\r\n<a href=\"#\" onabort=\"$(this).next().fadeIn(); return false;\">Display my next sibling<\/a>\r\n\r\n<a href=\"#\" ondurationchange=\"$(this).next().fadeIn(); return false;\">Display my next sibling<\/a>\r\n\r\n\r\n<a href=\"#\" onwaiting=\"$(this).next().fadeIn(); return false;\">Display my next sibling<\/a>\r\n\r\n\r\n<\/body>\r\n<\/html>"
}'
```
