from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('index/', views.index, name='index'),
    path('individual/<int:person_id>/', views.get_individual2, name='individual'),
]