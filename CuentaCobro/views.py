from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from CuentaCobro.serializers import CuentaCobroSerializer
from CuentaCobro.models import Cuenta_Cobro
 
class CuentaCobroViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Cuenta_Cobro.objects.all()
    serializer_class = CuentaCobroSerializer