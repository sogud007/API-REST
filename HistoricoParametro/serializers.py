from rest_framework_mongoengine import serializers
from HistoricoParametro.models import Historico_Parametros
 
class HistoricoParametrosSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Historico_Parametros
        fields = '__all__'