from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer


class ObtainTokenPairWithUserView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


token_obtain_pair = ObtainTokenPairWithUserView.as_view()
