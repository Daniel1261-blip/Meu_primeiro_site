from django.urls import path
from . import views

urlpatterns = [
    path('', views.testando),
    path('Boot/', views.boot),
]
