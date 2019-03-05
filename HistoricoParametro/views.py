from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from HistoricoParametro.serializers import HistoricoParametrosSerializer
from HistoricoParametro.models import Historico_Parametros
 
class HistoricoParametrosViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Historico_Parametros.objects.all()
    serializer_class = HistoricoParametrosSerializer