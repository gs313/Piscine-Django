from django.urls import path
from . import views

urlpatterns = [
    path('django/', views.django_page, name='django'),
    path('django', views.django_page, name='django'),
    path('display/', views.display_page, name='display'),
    path('display', views.display_page, name='display'),
    path('templates/', views.templates_page, name='templates'),
    path('templates', views.templates_page, name='templates'),
]
