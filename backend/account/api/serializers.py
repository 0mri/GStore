from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from djoser.serializers import UserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.conf import settings
# from backend.account.models import Profile
from backend.account.models import User


class PrivateUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'date_joined', 'profile_image']
        read_only_fields = ['username', 'date_joined']

    def update_profile_image(self, obj):
        user = self.context.get('request').user
        user.profile_image = obj['file']
        user.save()
        return user.profile_image.url


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': PrivateUserSerilizer(self.user).data})
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
