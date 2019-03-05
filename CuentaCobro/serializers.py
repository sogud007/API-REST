from rest_framework_mongoengine import serializers
from CuentaCobro.models import Cuenta_Cobro
 
class CuentaCobroSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Cuenta_Cobro
        fields = '__all__'