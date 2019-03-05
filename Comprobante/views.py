from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from Comprobante.serializers import ComprobantesSerializer
from Comprobante.models import Comprobantes
 
class ComprobantesViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Comprobantes.objects.all()
    serializer_class = ComprobantesSerializer