from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from Modulo.serializers import ModulosSerializer
from Modulo.models import Modulos
 
class ModulosViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Modulos.objects.all()
    serializer_class = ModulosSerializer