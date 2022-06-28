from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list_tunnels"),
    path('new/', views.new, name="new_tunnel"),
    path('edit/<int:pk>/', views.edit, name="edit_tunnel"),
    path('remove/<int:pk>/', views.remove, name="remove_tunnel")
]
