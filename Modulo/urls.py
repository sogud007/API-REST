from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from Modulo.views import ModulosViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'api', ModulosViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls