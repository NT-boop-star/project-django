from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    path('', views.adherent_list, name='adherent_list'),
    path('adherent/<int:pk>/', views.adherent_detail, name='adherent_detail'),
    path('adherent/ajouter/', views.adherent_create, name='adherent_create'),
    path('adherent/<int:pk>/modifier/', views.adherent_update, name='adherent_update'),
]