from rest_framework_mongoengine import serializers
from PropHorizontal.models import Propiedades_Horizontales
 
class PropHorizontalSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Propiedades_Horizontales
        fields = '__all__'