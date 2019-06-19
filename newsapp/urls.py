from . import views
from django.urls import path

urlpatterns = [
    path('', views.scrape, name='home'),
    path('index/',views.index,name = 'index'),
]