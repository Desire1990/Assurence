from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class TokenPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		data = super(TokenPairSerializer, self).validate(attrs)
		data['services'] = [group.name for group in self.user.groups.all()]
		data['is_admin'] = self.user.is_superuser
		data['id'] = self.user.id
		data['fullname'] = self.user.first_name+" "+self.user.last_name
		data['email'] = self.user.email
		return data

class RegisterSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

	class Meta:
		model = User
		fields = ('username','email', 'password', 'first_name', 'last_name')
		extra_kwargs = {
		    'first_name': {'required': True},
		    'last_name': {'required': True}
    	}

	def create(self, validated_data):
		user = User.objects.create(
			email=validated_data['email'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name']
		)

		user.set_password(validated_data['password'])
		user.save()

		return user


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = "__all__"
		
class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	profile = ProfileSerializer(required=True)
	email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

	class Meta:
		model = User
		exclude = "last_login","is_staff","date_joined","user_permissions"

class AutomobileSerializer( serializers.ModelSerializer):
	class Meta:
		model = Automobile
		fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = "__all__"
# class PhotoSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Photo
# 		fields = "__all__"
