from django.urls import path
from authapp import views

urlpatterns = [
    path('login/', views.login),
]
