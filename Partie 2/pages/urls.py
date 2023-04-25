from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('connexion/', views.login, name='login'),
    path('plantes/', views.plant_list, name='plantList'),
    path('plante/<int:plant_id>', views.plant_detail, name='plantDetail'),
    path('annonces/', views.offer_list, name='offerList'),
    path('annonces/ajouter', views.offer_add, name='offerAdd'),
    path('annonce/<int:offer_id>', views.offer_detail, name='offerDetail'),
    path('utilisateur/<int:user_id>', views.user_detail, name='userDetail'),
]
