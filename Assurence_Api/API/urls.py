from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register("profile", ProfileViewset)
router.register("pay", PaymentViewset)
router.register("automobile", AutomobileViewset)

urlpatterns = [
	path("", include(router.urls)),
	path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),

]