from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user(request):
    if request.method == 'GET':
        # getting user
        pass
    elif request.method == 'POST':
        # adding user
            # getting post args
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        superpower = request.POST['superpower']

        print username
        print password
        print email
        print firstname
        print lastname

        #creating user object
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.superpower = superpower
        user.save()
        return HttpResponse("ok")

    raise Http404("(-__-) 404!")
