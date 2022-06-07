from django.urls import path

from posts import views

urlpatterns = [
    path('', views.main, name='main'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
]