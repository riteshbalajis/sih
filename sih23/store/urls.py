from django.contrib import admin
from django.urls import include, path
from store import views
urlpatterns = [
    path('',views.showbussiness),
    path('storelogin/',views.showstorelogin),
    path('storesignout/',views.storesignout),
    path('storesignup',views.showstoresignup),
]