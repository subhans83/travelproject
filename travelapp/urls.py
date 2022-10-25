
from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo,name='demo'),
    path('about/', views.about,name='about'),
    path('contacts/', views.contacts,name='contacts')
]
