from rest_framework_mongoengine import serializers
from Cobro.models import Cobros
 
class CobrosSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Cobros
        fields = '__all__'