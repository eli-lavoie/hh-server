from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from habitAPI.models import Hero
from django.contrib.auth.models import User


#ANCHOR: User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name="user",
            lookup_field="id"
        )
        fields=(
            "id",
            "first_name",
            "last_name",
            "date_joined",
            "email"
        )

#ANCHOR: Hero Serializer
class HeroSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Hero
        url = serializers.HyperlinkedIdentityField(
            view_name="hero",
            lookup_field="id"
        )
        fields = (
            "id",
            "url",
            "user",
            "strength_level",
            "strength_exp",
            "dexterity_level",
            "dexterity_exp",
            "spirit_level",
            "spirit_exp",
            "intellect_level",
            "intellect_exp",
            "charm_level",
            "charm_exp",
            "title",
            "profile_picture_url",
            "credits_owned",
            "boss_damage",
            "prestige_level",
            "prestige_exp"
        )

#ANCHOR: Heroes viewset
class Heroes(ViewSet):
    def retrieve(self, request, pk=None):

        try:
            hero = Hero.objects.get(pk=pk)

            serializer = HeroSerializer(hero, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        heroes = Hero.objects.all()

        serializer = HeroSerializer(heroes, many=True, context={'request': request})

        return Response(serializer.data)