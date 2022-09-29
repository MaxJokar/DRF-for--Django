# Serializers allow complex data such as querysets and model instances to be converted to
# native Python datatypes that can then be easily rendered into JSON , XML or other content types
from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # need all fields from model
        fields = "__all__"


        #fields = ("title", "slug" ,"author", "content", "publish", "status") OR
        # the same as above using exclude
        # exclude = ("created" , "updated")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"




