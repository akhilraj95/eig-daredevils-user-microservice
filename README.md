# Eig-daredevils-user-microservice

eig-daredevils-user-microservice is a coordinating backend service. Two instances of this service will run, one each for Avengers and Xmen. It functions as the user management, authentication, authorization(JWT token), serve todos. The service also allows XMEN server to access AVENGERS todo with the correct digital signature and vice-versa. The service gives a redirect endpoint that logs the Avenger user to log in to Xmen server without re-entering the credentials.
    
  - User management 
  - Authentication
  - Authorization
  - Serve todos
  - Both instances(xmen and avenger) can access each others todo
  - Redirect to each others instance without re-entering the credentials


Architecture: 
![alt text][logo]

[logo]: https://github.com/akhilraj95/eig-daredevils-user-microservice/arch.png "architechture"


## Tech

Dillinger uses a number of open source projects to work properly:

* [Django] - Server
* [BeautifulSoup] - Cleaning html
* [PyJWT] - Generating and validating JWT tokens
* [requests] - Sending Requests
* [django-cors-headers] - Setting up CORS


## Installation

Clone the repository. Master branch is the Avenger Server and the xmen branch is the Xmen server.

Install the dependencies and set up the environment.

```sh
$ cd eig-daredevils-user-microservice
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ rm restserver/db.sqlite3
```

To run marvel

```sh
$ cd restserver
$ git checkout master
$ python manage.py runserver 0.0.0.0:8888
```

To run marvel

```sh
$ cd restserver
$ git checkout xmen
$ python manage.py runserver 0.0.0.0:9999
```

To set up CORS, edit restserver/restserver/settings.py

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

--------------------------------------------------------------------------------------------------------------------

## dashboard

### by curl
```
curl -X GET \
  http://127.0.0.1:8000/dashboard \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywiZ3JvdXBpZCI6ImF2ZW5nZXIiLCJ0aW1lIjoxNDk3NjAwNzAyfQ.13p2p2naArvI8U_n8P9zy4osEN43QA5gIG5AQpW3VU0' \
  -H 'cache-control: no-cache' \
```

----------------------------------------------------------------------------

## Sanitize

### By curl
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


--------------------------------------------------------------------------
## Bio 

### Get your bio
```
curl -X GET \
  http://0.0.0.0:9999/bio \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InhtZW4xIiwidXNlcmlkIjoxLCJncm91cGlkIjoiYXZlbmdlciIsInRpbWUiOjE0OTc3MDA4MzN9.jKW7TvrRkCtwZD42VgG1sNQw1PIaMOJliD3Cyv_Qdyg' \
```

### Update or create bio 
```
curl -X POST \
  http://0.0.0.0:9999/bio \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InhtZW4xIiwidXNlcmlkIjoxLCJncm91cGlkIjoiYXZlbmdlciIsInRpbWUiOjE0OTc3MDA4MzN9.jKW7TvrRkCtwZD42VgG1sNQw1PIaMOJliD3Cyv_Qdyg' \
  -H 'content-type: application/json' \
  -d '{
  "data":"<h1>spongebob is dead</h1><script></script>"
}'
```

### Get other bio
```
curl -X GET \
  http://0.0.0.0:8888/bio/spongebob \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywiZ3JvdXBpZCI6ImF2ZW5nZXIiLCJ0aW1lIjoxNDk3NzA2MTQyfQ.EJeFXqfUlVVlT1jLTi0cquAGlCDb6PYoE1JiN1rKEZ0' \
```

-----------------------------------------------------------------------

## External Do

### get Avenger todo from Xmen (or vice-versa)
```
curl -X GET \
  http://0.0.0.0:9999/xtodo \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6NywiZ3JvdXBpZCI6ImF2ZW5nZXIiLCJ0aW1lIjoxNDk3NzIwNjQ2fQ.FOhuiaPZWIY_LieBfuy5aHH5dW7TMN8M6wuGhTaA5CQ' \
```

------------------------------------------------------------------------

## Redirect url

### get a redirect url
```
curl -X GET \
  http://0.0.0.0:8888/redirect \
  -H 'accesstoken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywiZ3JvdXBpZCI6ImF2ZW5nZXIiLCJ0aW1lIjoxNDk3NzI1ODkzfQ.kioKs2nsU4-UH_Mqg2vq09vhMFxF60CGXLq9juTYi84' \
```