from django.urls import path
from . import views

app_name = "ceaser"   


urlpatterns = [
    path("main", views.main, name="main"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("cryption", views.cryption, name="cryption")
]