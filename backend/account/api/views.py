from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerilizer


class ObtainTokenPairWithUserView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


token_obtain_pair = ObtainTokenPairWithUserView.as_view()


class UploadProfileImage(APIView):
    parser_class = [FileUploadParser]

    def put(self, request, *args, **kwargs):
        file_serializer = UserSerilizer(context={'request': request}).update_profile_image(
            request.data)

        # print(request.data[])
        return Response(file_serializer)
        # file_serializer.save()
        # return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
