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
