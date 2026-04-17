from django.urls import path
from .views import signup_view, login_view, logout_view
from .views import logout_view


urlpatterns = [

    path("signup/", signup_view),
    path("login/", login_view),
    path("logout/", logout_view),
    path("logout/", logout_view),

]

from django.urls import path
from .views import login_view, signup_view, logout_view

urlpatterns = [
    path("login/", login_view),
    path("signup/", signup_view),
    path("logout/", logout_view),
]