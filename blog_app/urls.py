from django.urls import path
from blog_app import views


urlpatterns = [
    path('post/<int:pk>/', views.dummy, name='post_detail'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),

]
