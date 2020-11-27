import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from habitAPI.models import Hero


#ANCHOR: Login Function
@csrf_exempt
def login(request):
    '''Handles user authentication

    Method arguments:
        request -- the HTTP request object
    '''

    #HTTP Request string loaded into a dictionary
    req_body = json.loads(request.body.decode())
    
    #Server runs authentication function if request type is POST
    if request.method == 'POST':

        #Built in django user-authentication function
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        #If user credentials are correct, return the user's auth token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            userId = authenticated_user.id
            data = json.dumps({'valid': True, 'token': token.key, 'userId': userId})
            return HttpResponse(data, content_type='application/json')

        #Else return an invalid response
        else:
            data = ({'valid': False})
            return HttpResponse(data, content_type='application/json')

#ANCHOR: Register Function
@csrf_exempt
def register(request):
    '''Handles new user register

        Method arguments:
        request -- HTTP Request
    '''

    req_body = json.loads(request.body.decode())
    #Django function to create a new user object
    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password']
    )

    #Creates new hero instance with user foreignkey linked to new_user, all other values set to default model vals
    new_hero = Hero.objects.create(
        user=new_user
    )

    new_hero.save()

    token = Token.objects.create(user=new_user)
    userId = new_user.id

    data = json.dumps({'token': token.key, 'userId': userId})
    return HttpResponse(data, content_type='application/json')