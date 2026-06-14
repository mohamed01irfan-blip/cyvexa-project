from django.urls import path
from . import views
from .forms import BlogForm

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.create_blog, name='create_blog'),
    path('edit/<int:id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:id>/', views.delete_blog, name='delete_blog'),
    path('', views.blog_list, name='blog_list'),
path('login/', views.user_login, name='login'),
path('logout/', views.user_logout, name='logout'),

path('add-event/', views.add_event, name='add_event'),
path('edit-event/<int:id>/', views.edit_event, name='edit_event'),
path('delete-event/<int:id>/', views.delete_event, name='delete_event'),
]