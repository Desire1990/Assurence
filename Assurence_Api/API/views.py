from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.response import Response
from .models import *
from .serializers import *

class ProfileViewset(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer


class AutomobileViewset(viewsets.ModelViewSet):
	queryset = Automobile.objects.all()
	serializer_class = AutomobileSerializer

	
class PaymentViewset(viewsets.ModelViewSet):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer
	
# class PhotoViewset(viewsets.ModelViewSet):
# 	queryset = Photo.objects.all()
# 	serializer_class = PhotoSerializer
