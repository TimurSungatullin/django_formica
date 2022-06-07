from django.conf.urls.static import static
from django.urls import path

from authorization import views
from django_formica.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)