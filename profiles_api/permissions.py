from rest_framework import permissions 


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, virw, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        # check wheather the object they're updating matches their authentication user profile
        # that is added to the authentication of the request 
        return obj.id == request.user.id 