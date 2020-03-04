from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from blog.models import Page
from api.serializers import PageSerializers


class PostList(APIView):
    def get(self, request):
        pages = Page.objects.all()[:20]
        data = PageSerializers(pages, many=True).data
        return Response(data)


class PostDetail(APIView):
    def get(self, request, pk):
        page = get_object_or_404(Page, pk=pk)
        data = PageSerializers(page).data
        return Response(data)


class PostCreate(APIView):
    def post(self, request):
        form = PageForm(request.POST)
        data = PageSerializers(form).data
        return Response(data)
