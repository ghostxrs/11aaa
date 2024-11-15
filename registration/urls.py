from registration.views import *
from django.urls import path
urlpatterns = [
    path('logout', user_logout, name='logout'),
    path('', SignUp.as_view(), name='signup'),
]

