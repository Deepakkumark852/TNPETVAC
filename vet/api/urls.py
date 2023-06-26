from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('owners/', views.ownersList),
    path('owner/<str:pk>/', views.ownerDetail),
    path('owners/create/', views.ownerCreate),
    path('owners/update/<str:pk>/', views.ownerUpdate),
    path('owners/delete/<str:pk>/', views.ownerDelete),
    path('pets/', views.petsList),
    path('pet/<str:pk>/', views.petDetail),
    path('pets/create/', views.petCreate),
    path('pets/update/<str:pk>/', views.petUpdate),
    path('pets/delete/<str:pk>/', views.petDelete),
]