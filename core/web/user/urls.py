from django.urls import path

from core.web.user.views import profile, login, register, logout


app_name = "user"
urlpatterns = [
    path("profile/", profile, name="profile"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
]
