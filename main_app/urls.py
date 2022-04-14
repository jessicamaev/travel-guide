from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('cities/', views.cities_index, name='cities_index'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
    path('cities/create/', views.CityCreate.as_view(), name='city_create'),
    path('cities/<int:pk>/update/', views.CityUpdate.as_view(), name='city_update'),
    path('cities/<int:pk>/delete/', views.CityDelete.as_view(), name='city_delete'),
    path('experiences/', views.experiences_index, name='experiences_index'),
    path('experiences/<int:experience_id>/', views.experience_detail, name='experience_detail'),
    path('experiences/create/', views.experiences_create, name='experience_create'),
    path('experiences/<int:pk>/update/', views.ExperienceUpdate.as_view(), name='experience_update'),
    path('experiences/<int:pk>/delete/', views.ExperienceDelete.as_view(), name='experience_delete'),
    path('cities/<int:city_id>/add_photo/', views.add_photo, name='add_photo'),
]

