from rest_framework_mongoengine import serializers
from Noticia.models import Noticias
 
class NoticiasSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Noticias
        fields = '__all__'