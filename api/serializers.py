from rest_framework.serializers import ModelSerializer

from blog.models import Page


class PageSerializers(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

