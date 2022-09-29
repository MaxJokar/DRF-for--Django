from rest_framework.permissions import BasePermission ,SAFE_METHODS

"""
To make a private permission for views we do following
"""
# IsAdminUser was before
class IsSuperUser(BasePermission):
    """
    Allows access only to Superusers.
    """
    def has_permission(self, request, view):
        #if login and superUser access All
        return bool(request.user and request.user.is_superuser)

# like is_Authenticated or Readonly:default permission:
# Users registered can not change only staff
class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            # log in
            request.user and
            # request.user.is_authenticated
            request.user.is_staff
        )

# if User safe , allowed  ReadOnly else if that objects Author is this User or not
# from the django REST framework cope the following(IsOwnerOrReadOnly) to author
class IsAuthorOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        # return obj.owner == request.user
        # from our Article the field author, be able to change the Article
        #return obj.author == request.user
        return bool(
            # else if that objects Author is this User or not
            # checks that objects Author is
            #get access to superuser
            request.user.is_authenticated and
            request.user.is_superuser or
            # object is the USER is seeing the page
            # get access to author of object
            obj.author == request.user


        )



# A Hybric Permission following:
# if method safe and that User is Staff just can see
class IsSuperUserOrStaffReadOnly(BasePermission):
    """
    if SuperUser:all aceess,Staff:ReadOnly,Rest staff:No access at All
    """
    def has_permission(self, request, view):
        # # If Safe_Method and the USER is Staff, return
        # if request.method in SAFE_METHODS and \
        # request.user.is_authenticated  and \
        # request.user.is_staff :
        #     return True

        # Instance must have an attribute named `owner`.
        # return obj.owner == request.user
        # from our Article the field author, be able to change the Article
        #return obj.author == request.user
        return bool(
            #get access to superuser
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_staff or
            # if User is  Super can access all
            request.user and
            request.user.is_superuser


        )
