from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from Parametro.views import ParametrosViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'api', ParametrosViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls