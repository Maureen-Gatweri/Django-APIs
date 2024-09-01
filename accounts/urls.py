from django.urls import path
from .views import login
from .views import logout
from . import views

urlpatterns=[
    path ('login/', views.login, name=login),
    path ('logout/', views.logout, name=logout),
    # path ('home/', views.home, home= home)
]