from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cities/', views.cities_index, name='cities_index'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
    path('cities/create/', views.CityCreate.as_view(), name='city_create'),
    path('cities/<int:pk>/update/', views.CityUpdate.as_view(), name='city_update'),
    path('cities/<int:pk>/delete/', views.CityDelete.as_view(), name='city_delete'),
    path('experiences/', views.experiences_index, name='experiences_index'),
    path('experiences/create/', views.ExperienceCreate.as_view(), name='experience_create'),
    path('cities/<int:city_id>/add_photo/', views.add_photo, name='add_photo'),

]

