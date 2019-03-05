from rest_framework_mongoengine import serializers
from Comprobante.models import Comprobantes
 
class ComprobantesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Comprobantes
        fields = '__all__'