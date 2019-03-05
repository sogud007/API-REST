from rest_framework_mongoengine import serializers
from UnidadPrivada.models import Unidades_Privadas
 
class UnidadesPrivadasSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Unidades_Privadas
        fields = '__all__'