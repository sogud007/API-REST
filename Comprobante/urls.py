from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from Comprobante.views import ComprobantesViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'api', ComprobantesViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls