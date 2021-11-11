from django.urls import path
from .views import user_list, PostList, PostDetail

urlpatterns = [
    path('users',user_list),
    path('posts', PostList.as_view()),
    path('posts/<int:id>', PostDetail.as_view())
]