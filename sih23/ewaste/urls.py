from django.contrib import admin
from django.urls import path
from ewaste import views
urlpatterns = [
    path('',views.showhome),
    path('userlogin/',views.showuserlogin),
    path('signup/',views.showsignup),
    path('logout/',views.signout),
    path('users/',views.showuserdetails),
    path('profile/',views.showprofile),
    path('shops/',views.showshops),
]