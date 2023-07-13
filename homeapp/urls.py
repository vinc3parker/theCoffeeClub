from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('your_journey/', views.your_journey, name='your_journey'),
    path('new_review/', views.new_review, name='new_review'),
]
