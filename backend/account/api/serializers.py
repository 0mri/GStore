from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from djoser.serializers import UserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserDetailsSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': CustomUserDetailsSerializer(self.user).data})
        # and everything else you want to send in the response
        return data


# class CustomRegisterSerializer(RegisterSerializer):

#     email = serializers.EmailField(required=True)
#     password1 = serializers.CharField(write_only=True)
#     name = serializers.CharField(required=True)
#     date_of_birth = serializers.DateField(required=True)

#     def get_cleaned_data(self):
#         super(CustomRegisterSerializer, self).get_cleaned_data()

#         return {
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#             'name': self.validated_data.get('name', ''),
#             'date_of_birth': self.validated_data.get('date_of_birth', ''),
#         }
