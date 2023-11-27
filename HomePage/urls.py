from django.urls import path, include
from . import views
app_name='HomePage'
urlpatterns = [
    path('', views.home, name='home')
]
