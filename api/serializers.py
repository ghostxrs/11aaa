from rest_framework.serializers import ModelSerializer
from app.models import News

class New_serializer(ModelSerializer):
    class Meta:
        model = News
        fields = [
            'category',
            'region',
            'title',
            'body',
            'date',
            'image',
            'author'
        ]
        # depth = 1