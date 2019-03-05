from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from PropHorizontal.serializers import PropHorizontalSerializer
from PropHorizontal.models import Propiedades_Horizontales
 
class PropHorizontalViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Propiedades_Horizontales.objects.all()
    serializer_class = PropHorizontalSerializer