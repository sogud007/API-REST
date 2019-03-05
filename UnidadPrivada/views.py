from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from UnidadPrivada.serializers import UnidadesPrivadasSerializer
from UnidadPrivada.models import Unidades_Privadas
 
class UnidadesPrivadasViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Unidades_Privadas.objects.all()
    serializer_class = UnidadesPrivadasSerializer