from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from UnidadPrivada.views import UnidadesPrivadasViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'api', UnidadesPrivadasViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls