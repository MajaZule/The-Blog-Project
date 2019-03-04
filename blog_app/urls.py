from django.urls import path
from blog_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('aboutRamblog/', views.AboutBlogView.as_view(), name='about_blog'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/gallery/', views.GalleryListView.as_view(), name='gallery'),
]
