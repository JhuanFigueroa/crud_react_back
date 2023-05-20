from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name='mainapp_app'
urlpatterns = [
    path('',views.InicioView.as_view(),name='inicio'),
    path('api/actividades',views.getUsers().as_view()),
    path('api/actividades/detail/<pk>',views.detailUser().as_view()),
    path('api/actividades/create',views.createUser().as_view()),
    path('api/actividades/update/<pk>',views.updateUser().as_view()),
    path('api/actividades/delete/<pk>',views.deleteUser().as_view()),
  
   path('api/categorias',views.getCategorias().as_view()),
   path('api/categorias/<pk>',views.actividadByCategory().as_view()),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)