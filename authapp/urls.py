from django.urls import path
from authapp import views

urlpatterns = [
    path('user_token/', views.user_token),
]
