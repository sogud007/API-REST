from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from Cobro.serializers import CobrosSerializer
from Cobro.models import Cobros
 
class CobrosViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Cobros.objects.all()
    serializer_class = CobrosSerializer