from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView, View



from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView)


from .models import Categoria, Actividad

from .serializers import ActividadSerializer,ActividadDetailSerializer,CategoriaSerializer,CategoriaDetailSerializer

# Create your views here.


class InicioView(TemplateView):
    template_name = "index.html"


class getUsers(ListAPIView):
    serializer_class = ActividadDetailSerializer

    def get_queryset(self):
        return Actividad.objects.all()

class detailUser(RetrieveAPIView):
    queryset=Actividad.objects.all()
    serializer_class = ActividadSerializer
    


class createUser(CreateAPIView):
    serializer_class = ActividadSerializer


class updateUser(RetrieveUpdateAPIView):

    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()


class deleteUser(DestroyAPIView):
    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()

#Categorias
class getCategorias(ListAPIView):
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.all()

class actividadByCategory(RetrieveAPIView):
    serializer_class = CategoriaDetailSerializer
    queryset=Categoria.objects.all()
    