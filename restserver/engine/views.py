from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.contrib.auth import authenticate
import jwt
import time
from models import AccessToken
from django.http import QueryDict


APPSECRET = "DAREDEVIL2017"

@csrf_exempt
def user(request):
    if request.method == 'GET':
        pass
        # getting user  ---- DEBUG ONLY
        # users = User.objects.all().select_related('profile')
        # return HttpResponse(json.dumps([{'userid' : usr.id,
        #                                  'username': usr.username,
        #                                  'email' : usr.email} for usr in users]),
        #                      content_type='application/json')
    elif request.method == 'POST':
        # adding user
        try:
            #getting post args
            received_json_data=json.loads(request.POST['data'])

            username = received_json_data['username']
            password = received_json_data['password']
            email = received_json_data['email']
            firstname = received_json_data['firstname']
            lastname = received_json_data['lastname']
            superpower = received_json_data['superpower']

            #creating user object
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.profile.superpower = superpower
            user.profile.xmen = False
            user.profile.avenger = True
            user.save()
            return HttpResponse(status=201)
        except:
            return HttpResponse(status=500)
    raise Http404("(-__-) 404!")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        # creating AWT token
            # getting post args
            received_json_data=json.loads(request.POST['data'])

            username = received_json_data['username']
            password = received_json_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # # A backend authenticated the credentials
                encoded = jwt.encode({'userid': user.id,
                                      'username': user.username,
                                      'time': int(time.time())
                                     }, APPSECRET, algorithm='HS256')

                AccessToken.objects.create(user = user, jwt=encoded);
                data = json.dumps({ 'userid' : user.id,
                                    'username': user.username,
                                    'accesstoken': encoded
                                 })
                return HttpResponse(data,content_type='application/json',status=202)
            else:
                return HttpResponse(status=400)
    if request.method == 'DELETE':
        # try:
            accesstoken = request.META.get('HTTP_ACCESSTOKEN')
            print accesstoken
            jwt.decode(accesstoken, APPSECRET , algorithms=['HS256'])
            AccessToken.objects.get(jwt=accesstoken).delete()
            return HttpResponse(status=200)
        # except:
        #     return HttpResponse(status=400)
    raise Http404("(-__-) 404!")


def squad(request):
    if request.method == 'GET':
        users = User.objects.all().select_related('profile')
        return HttpResponse(json.dumps([{'userid' : usr.id,
                                         'username': usr.username,
                                         'email' : usr.email} for usr in users]),
                             content_type='application/json')
