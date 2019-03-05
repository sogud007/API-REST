from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from Noticia.serializers import NoticiasSerializer
from Noticia.models import Noticias
 
class NoticiasViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer
