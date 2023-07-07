from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('cuisines/', views.CuisineList.as_view(), name="cuisine_list"),
    path('cuisines/new/', views.CuisineCreate.as_view(), name="cuisine_create"),
    path('cuisines/<int:pk>/', views.CuisineDetail.as_view(), name="cuisine_detail"),
    path('cuisines/<int:pk>/update',views.CuisineUpdate.as_view(), name="cuisine_update"),
    path('cuisines/<int:pk>/delete',views.CuisineDelete.as_view(), name="cuisine_delete"),
]