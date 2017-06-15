# eig-daredevils-user-microservice
user microservice


## create user

```
curl -X POST \
  http://127.0.0.1:8000/user \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -d 'username=spiderman&email=spidey%40endurance.com&password=spidey&firstname=peter&lastname=parker&superpower=spider%20power'
```

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
      "username": "spiderman",
      "email": "spidey@endurance.com",
      "password": "spidey",
      "firstname": "peter",
      "lastname": "parker",
      "superpower": "spider power"
    }
  }

  $.ajax(settings).done(function (response) {
    console.log(response);
  });
```
