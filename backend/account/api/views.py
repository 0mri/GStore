from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PrivateUserSerilizer


class ObtainTokenPairWithUserView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


token_obtain_pair = ObtainTokenPairWithUserView.as_view()

