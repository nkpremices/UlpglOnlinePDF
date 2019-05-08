from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('datails/<categorie>/', views.details, name = 'details'),
    path('datails/', views.details, name = 'details'),
    path('fileUpload/',views.upload, name='upload'),
    path('search/',views.search, name='search'),


]

