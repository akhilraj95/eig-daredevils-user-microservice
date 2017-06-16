# eig-daredevils-user-microservice
user microservice


## create user

### request

#### by curl
```
curl -X POST \
  http://127.0.0.1:8000/user \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -d data=%7B%22username%22%20%3A%20%22wolverine%22%2C%20%22password%22%20%3A%20%22wolverinepass%22%2C%22email%22%20%3A%20%22wolverine%40endurance.com%22%2C%22firstname%22%20%3A%20%22wolverine%22%2C%22lastname%22%20%3A%20%22wolf%22%2C%22superpower%22%20%3A%20%22claws%22%7D
```

#### by AJAX
```
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://127.0.0.1:8000/user",
  "method": "POST",
  "headers": {
    "content-type": "application/x-www-form-urlencoded",
    "cache-control": "no-cache",
  },
  "data": {
    "data": "{\"username\" : \"wolverine\", \"password\" : \"wolverinepass\",\"email\" : \"wolverine@endurance.com\",\"firstname\" : \"wolverine\",\"lastname\" : \"wolf\",\"superpower\" : \"claws\"}"
  }
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
