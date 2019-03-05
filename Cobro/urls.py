from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from Cobro.views import CobrosViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'api', CobrosViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls