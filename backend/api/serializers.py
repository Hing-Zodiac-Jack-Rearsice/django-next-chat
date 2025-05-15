from rest_framework import serializers
# imports the built in django user model, if not i need to create my own user model
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object): 
        model = User
        fields = ['id','username','password','email']