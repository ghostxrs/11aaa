from django.urls import path

from .views import *

urlpatterns = [
    path('', List_view.as_view(), name='list'),
    path('<int:pk>', Detail_view.as_view(), name='detail')
]