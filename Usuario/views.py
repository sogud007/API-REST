from django.shortcuts import render
 
from rest_framework_mongoengine import viewsets, generics
from Usuario.serializers import UsuariosSerializer
from Usuario.models import Usuarios
 
#class CreateUsuarioViewSet(generics.ListCreateAPIView):
class UsuarioViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    
    '''
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    
    def perform_create(self, serializer):
        serializer.save()
    '''