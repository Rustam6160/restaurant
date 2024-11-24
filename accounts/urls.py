from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/', ProfileView.as_view(), name='profile'),

]