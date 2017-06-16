# eig-daredevils-user-microservice
user microservice


## create user

### by curl
```
curl -X POST \
  http://127.0.0.1:8000/user \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -d data=%7B%22username%22%20%3A%20%22wolverine%22%2C%20%22password%22%20%3A%20%22wolverinepass%22%2C%22email%22%20%3A%20%22wolverine%40endurance.com%22%2C%22firstname%22%20%3A%20%22wolverine%22%2C%22lastname%22%20%3A%20%22wolf%22%2C%22superpower%22%20%3A%20%22claws%22%7D
```

### by AJAX
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


## authenticate

### by curl
```
curl -X POST \
  http://127.0.0.1:8000/authenticate \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -d data=%7B%22username%22%3A%22spongebob%22%2C%22password%22%3A%22spongebob%22%7D
```

### by ajax
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

## logout

### by curl
```
curl -X DELETE \
  http://127.0.0.1:8000/authenticate \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -d data=%7B%22accesstoken%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywidGltZSI6MTQ5NzU4NDU4NX0.czW23GyLdVpgnAXWF67BaFzdIBYCn4eXgdI4OGpwCGE%22%7D
```
### by ajax
```
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://127.0.0.1:8000/authenticate",
  "method": "DELETE",
  "headers": {
    "content-type": "application/x-www-form-urlencoded",
    "cache-control": "no-cache",
  },
  "data": {
    "data": "{\"accesstoken\":\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNwb25nZWJvYiIsInVzZXJpZCI6MywidGltZSI6MTQ5NzU4NDU4NX0.czW23GyLdVpgnAXWF67BaFzdIBYCn4eXgdI4OGpwCGE\"}"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```
