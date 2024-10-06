from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.main),
    path('index/', views.index),
    path('book/', views.book),
    path('news/', views.book),
    path('user/', views.book),
]
