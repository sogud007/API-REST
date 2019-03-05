from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from HistoricoParametro.views import HistoricoParametrosViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'api', HistoricoParametrosViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls