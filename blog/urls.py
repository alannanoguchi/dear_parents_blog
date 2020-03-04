from django.urls import path, include
from blog.views import PostListView, PostDetailView, PostCreateView



urlpatterns = [
    path('api/', include('api.urls')),
    path('', PostListView.as_view(), name='blog-list-page'),
    path('<str:slug>/', PostDetailView.as_view(), name='blog-details-page'),
    path('new', PostCreateView.as_view(), name='new-page'),
]