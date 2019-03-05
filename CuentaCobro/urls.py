from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from CuentaCobro.views import CuentaCobroViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'api', CuentaCobroViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls