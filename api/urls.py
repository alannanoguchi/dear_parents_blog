from django.urls import path

from api.views import PostCreate, PostList, PostDetail

urlpatterns = [
    path('blog/', PostList.as_view(), name='page_list'),
    path('blog/<int:pk>', PostDetail.as_view(), name = 'page_detail'),
    path('blog/new', PostCreate.as_view(), name = 'new_page'),

]