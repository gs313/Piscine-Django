from django.urls import path
from . import views

urlpatterns = [
    path('', views.shades_view, name='shades'),
]
