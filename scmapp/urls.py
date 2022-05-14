
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("user_reg",views.user_reg,name="user_reg"),
    path("user_test",views.user_test,name="user_test"),
    path("user_login",views.user_login,name="user_login"),
    path("user_check",views.user_check,name="user_check"),
    path("ground_booking",views.ground_booking,name="ground_booking"),
    path("data_ground_booking",views.data_ground_booking,name="data_ground_booking"),
    path("admin_login_page",views.admin_login_page,name="admin_login_page"),
    path("admin_check",views.admin_check,name="admin_check"),
    path("admin_booking",views.admin_booking,name="admin_booking")
]
