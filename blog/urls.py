from django.urls import path
# from blog.views import PostListView,PostDetailView
    # , create_post, delete_post
from blog import views

app_name = 'blogs'

urlpatterns = [

    # path("",PostListView.as_view(),name='post_list'),
    # path('blog/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    # path('blog/create/', create_post, name='create_post'),
    # path('blog/<int:id>/delete', delete_post, name='delete_post'),
    path('',views.list_post,name="listpost")



]