from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import New_serializer
from app.models import News
# Create your views here.

class List_view(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = New_serializer

class Detail_view(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = New_serializer