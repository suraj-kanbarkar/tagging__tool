from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^read/', views.tagged_text),
    url(r'^tagged_text/', views.tagged_text, name='tagged_text'),
    url(r'^data/', views.read),
]
