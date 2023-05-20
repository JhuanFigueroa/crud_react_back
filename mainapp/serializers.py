from rest_framework import serializers

from .models import Actividad,Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields=('__all__')

class ActividadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Actividad
        fields=(
            'id',
            'nombre',
            'fecha',
            'participantes',
            'objetivo',
            'descripcion',
            'categoria',
            'imagen'
        )

class ActividadDetailSerializer(serializers.ModelSerializer):
    categoria=CategoriaSerializer()
    class Meta:
        model=Actividad
        fields=(
            'id',
            'nombre',
            'fecha',
            'participantes',
            'objetivo',
            'descripcion',
            'categoria',
            'imagen',
            'categoria'
        )

class CategoriaDetailSerializer(serializers.ModelSerializer):
    actividades=ActividadSerializer(many=True,read_only=True)
    class Meta:
        model=Categoria
        fields=(
            'id',
            'descripcion',
            'actividades',
        )