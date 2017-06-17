from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.contrib.auth import authenticate
import jwt
import time
from models import AccessToken,Bio
from django.http import QueryDict
from models import Profile
import requests
import BeautifulSoup as bs4
import re

APPSECRET = "DAREDEVIL2017"
todo_server_url = "http://10.128.5.116:3000"
get_todo_url = todo_server_url+"/todos/"




def default_html():
    html = """<h4>welcome to your default bio.</h4>"""
    return html

# Verify the JWT token
def accessTokenVerify(request):
    accesstoken = request.META.get('HTTP_ACCESSTOKEN')
    decodedjson = jwt.decode(accesstoken, APPSECRET , algorithms=['HS256'])
    # print decodedjson['username']
    userid = decodedjson['userid']
    groupid = decodedjson['groupid']
    user = User.objects.get(id = userid)
    num_results = AccessToken.objects.filter(user = user, jwt = accesstoken).count()
    if num_results == 0:
        raise Exception("Invalid JWT");    
    return userid,groupid



def cleanHTML(rawtext):
    soup = bs4.BeautifulSoup(str(rawtext))
    try:
        soup.script.decompose()
    except:
        print "no script"
    try:
        soup.form.decompose()
    except:
        print "no form"
    try:
        soup.button.decompose()
    except:
        print "no button"
    try:
        soup.link.decompose()
    except:
        print "no link"
    text = str(soup)
    text = re.sub(r'on(.)+=(\s)*"(.)+"', '', text)
    return text



@csrf_exempt
def user(request):
    if request.method == 'POST':
        # adding user
        try:
            #getting post args
            print request.body
            received_json_data=json.loads(request.body)["data"]

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
            received_json_data=json.loads(request.body)["data"]

            username = received_json_data['username']
            password = received_json_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # # A backend authenticated the credentials
                encoded = jwt.encode({'userid': user.id,
                                      'username': user.username,
                                      'groupid' : "avenger",
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
        try:
            accesstoken = request.META.get('HTTP_ACCESSTOKEN')
            jwt.decode(accesstoken, APPSECRET , algorithms=['HS256'])
            AccessToken.objects.get(jwt=accesstoken).delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)
    raise Http404("(-__-) 404!")


@csrf_exempt
def dashboard(request):
    if request.method == 'GET':
        try:
            userid,groupid = accessTokenVerify(request)

            #getting squad information
            squad = User.objects.all().exclude(id__in=[userid,2]).select_related("profile")
            profiles = Profile.objects.all()

            usr = squad[1]
            print profiles.get(user = usr).superpower
            squad_json = [{'userid' : usr.id,
                                      'username': usr.username,
                                      'email' : usr.email,
                                      'firstname': usr.first_name,
                                      'lastname': usr.last_name,
                                      'superpower': profiles.filter(user = usr)[0].superpower,
                                      'avenger': profiles.filter(user = usr)[0].avenger,
                                      'xmen': profiles.filter(user = usr)[0].xmen } for usr in squad]

            #getting todos both personal and group
            querystring = {"userid":userid,"groupid":groupid}
            headers = {
                'cache-control': "no-cache",
                }
            response = requests.request("GET", get_todo_url, headers=headers, params=querystring)
            todo_json = json.loads(response.text)

            data = {}
            data['squad'] = squad_json
            data['todo'] = todo_json["message"]

            return HttpResponse(json.dumps(data),status=200 ,content_type='application/json')
        except:
            return HttpResponse(status=400)

# TODO: Update todo
@csrf_exempt
def todo(request):
    if request.method == 'POST':
        try:
            userid,groupid = accessTokenVerify(request)

            received_json_data=json.loads(request.body)
            description = received_json_data["description"]
            status = received_json_data["status"]
            type_var = received_json_data["type"]

            url = "http://10.128.5.116:3000/todos"

            payload = "{\n\t\"description\" : \""+description+"\",\n\t\"status\" : \""+status+"\",\n\t\"type\" : \""+type_var+"\",\n\t\"userid\" : \""+str(userid)+"\",\n\t\"groupid\" : \""+str(groupid)+"\"\n}"
            headers = {
                'content-type': "application/json",
                }

            response = requests.request("POST", url, data=payload, headers=headers)

            print(response.text)
            print(response.headers)
            if response.status_code == 201:
                return HttpResponse(status=201)
            else:
                return HttpResponse(status=500)
        except:
            return HttpResponse(status=400)
    elif request.method == 'PUT':
        userid,groupid = accessTokenVerify(request)
        received_json_data=json.loads(request.body)
        description = received_json_data["description"]
        status = received_json_data["status"]
        type_var = received_json_data["type"]
        type_var = received_json_data["id"]

        return HttpResponse(status=200)
    return HttpResponse(status=404)


@csrf_exempt
def bio(request):
    if request.method == 'GET':
        userid,groupid = accessTokenVerify(request)
        user = User.objects.get(id = userid)
        bio = Bio.objects.filter(user = user)
        if bio.count() == 0:
            return HttpResponse(default_html(),status=200)
        else:
            return HttpResponse(bio[0].html,status=200)
    elif request.method == 'POST':
        # try:
            userid,groupid = accessTokenVerify(request)
            received_json_data=json.loads(request.body)
            html = received_json_data["data"]
            html = cleanHTML(html)
            user = User.objects.get(id=userid)
            bios = Bio.objects.filter(user = user)
            if(bios.count == 0):
                Bio.objects.create(user=user,html=html)
            else:
                b = Bio.objects.get(user=user)
                b.html = html
                b.save()
            return HttpResponse(status=200)
        # except:
        #     return HttpResponse(status=400)
    return HttpResponse(status=400)



@csrf_exempt
def sanitize(request):
    if request.method == 'POST':
            userid,groupid = accessTokenVerify(request)
            received_json_data=json.loads(request.body)
            html = received_json_data["data"]
            html = cleanHTML(html)
            return HttpResponse(html,status=200)
        
    return HttpResponse(status=400)





