from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register("profile", ProfileViewset)
# router.register("photo", PhotoViewset)
router.register("pay", PaymentViewset)
router.register("automobile", AutomobileViewset)

urlpatterns = [
	path("", include(router.urls)),
]