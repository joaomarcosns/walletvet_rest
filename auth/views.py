
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from auth.serializers.login_serializer import AuthTokenSerializer
from users.serializers.get_serializers import UserListSerializers



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(
            data=request.data,
            context={"request": request}
        )
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        response = UserListSerializers(user).data
        response["token"] = token.key

        return Response(response)

