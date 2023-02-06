from django.urls import path, include
#from .views import PostList, PostDetail, CommentList, CommentDetail

urlpatterns = [
    path('tabel/', include('tabel.urls')),
    #path('posts/', PostList.as_view()),
    #path('posts/<int:pk>/', PostDetail.as_view()),
    #path('comments/', CommentList.as_view()),
    #path('comments/<int:pk>/', CommentDetail.as_view()),
]