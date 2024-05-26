from rest_framework.viewsets import ViewSet
from core.auth.serializers import RegisterSerializer
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


class RegisterViewSet(ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['post']

    # define create action to bound with post method
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # save user to the db

        # adding token logic for authentication
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response(data={
            "user": serializer.data,
            "refresh": res["refresh"],
            "access": res["access"]
        }, status=status.HTTP_201_CREATED)





