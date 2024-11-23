from django.urls import path
from .views import *


urlpatterns = [
    path('sign_in/', LoginUserView.as_view(), name='sign_in'),
    path('register/', RegisterUserView.as_view(), name='register'),
]