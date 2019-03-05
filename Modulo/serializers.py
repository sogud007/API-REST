from rest_framework_mongoengine import serializers
from Modulo.models import Modulos
 
class ModulosSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Modulos
        fields = '__all__'