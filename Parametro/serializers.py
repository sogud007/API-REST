from rest_framework_mongoengine import serializers
from Parametro.models import Parametros
 
class ParametrosSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Parametros
        fields = '__all__'