from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LoginAPIView, RegistrationAPIView, CarShareUserView


app_name = 'users'

router = DefaultRouter()
router.register('user', CarShareUserView, basename='user')

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='user_registration'),
    path('login/', LoginAPIView.as_view(), name='user_login')
]

urlpatterns += router.urls
