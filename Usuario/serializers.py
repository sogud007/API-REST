from rest_framework_mongoengine import serializers
from Usuario.models import Usuarios
 
class UsuariosSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'