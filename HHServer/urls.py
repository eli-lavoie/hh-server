from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from habitAPI.views import register, login
from habitAPI.views import *

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'heroes', Heroes, 'hero')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register),
    path('login/', login),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
