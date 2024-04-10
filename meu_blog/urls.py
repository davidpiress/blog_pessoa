from django.urls import path
from . import views

app_name = 'meu_blog'

urlpatterns = [
    path('', views.welcome, name='welcome')
]
