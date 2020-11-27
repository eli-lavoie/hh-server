#TODO: Create user serializer
#TODO: Create hero serializer
#TODO: Create heroes viewset

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from habitAPI.models import Hero
from django.contrib.auth.models import User