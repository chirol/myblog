from django.urls import path, include
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.PostView.as_view(), name='index')
]
