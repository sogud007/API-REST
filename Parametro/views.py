from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from Parametro.serializers import ParametrosSerializer
from Parametro.models import Parametros
 
class ParametrosViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Parametros.objects.all()
    serializer_class = ParametrosSerializer