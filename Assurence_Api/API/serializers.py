from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = "__all__"
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
