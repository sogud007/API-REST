from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from Noticia.views import NoticiasViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'api', NoticiasViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls