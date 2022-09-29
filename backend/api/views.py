from django.contrib.auth.models import User
# ListAPIView: Used for read-only endpoints to represent a collection of model instances.
# Provides a get method handler.
# Extends: GenericAPIView, ListModelMixin.
#  ListCreateAPIView # gives a part to create API
from rest_framework.generics import ListAPIView ,ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# To avoid Error more than amount of our articels we use the following
from rest_framework.generics import RetrieveAPIView
# ArticleSerializer: gives you a powerful, generic way to control the output of your responses,
# as well as a ModelSerializer .
from .serializers import ArticleSerializer , UserSerializer
from blog.models import Article
# IsSuperUser ,
from .permissions import  IsAuthorOrReadOnly,IsStaffOrReadOnly ,IsSuperUserOrStaffReadOnly


class ArticleList(ListCreateAPIView):
        # QuerySet represents a collection of objects from your database.
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer


# class ArticleDetail(DestroyAPIView):we won't see the content ,delete button
#To have ability to dele te and  show the deleted item , we can use from :RDAV (RetrieveDestroyAPI )
# to update we can use (UPdateAPIView) to rewrite fields
# (RetrieveUpdateAPIView) for : GET , PUT , UPDATE
# More complete one is :ReitreveUpdateDestroyAPIView
class ArticleDetail(RetrieveUpdateDestroyAPIView):
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer
        # the field which is supposed to be looked up
        # (based on its kwargs arguemt) our object be selected
        #lookup_field = "slug" # by default primary key "pk"
        # we mixed isstaffreadOnly with AuthorReadOnly !!!
        permission_classes = (IsStaffOrReadOnly,IsAuthorOrReadOnly)



# Only AdminUSERs  can see USERsDetails & USERList
from rest_framework.permissions import IsAdminUser

class UserList(ListCreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        #permission_classes = (IsAdminUser,)
        # permission_classes = (IsSuperUser,)
        permission_classes = (IsSuperUserOrStaffReadOnly,)



class UserDetail(RetrieveAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        #permission_classes = (IsAdminUser,)
        # permission_classes = (IsSuperUser,)
        permission_classes = (IsSuperUserOrStaffReadOnly,)

#After we run : 127.0.0:8000/api/users we can see : list of our USERS



