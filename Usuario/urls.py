from django.conf.urls import url
from rest_framework_mongoengine import routers
from Usuario.views import UsuarioViewSet
 
routers = routers.DefaultRouter()
routers.register(r'api', UsuarioViewSet)
#routers.register(r'api', CreateUsuarioViewSet)
#routers.register(r'api/$', CreateUsuarioViewSet.as_view(), "create")
 
urlpatterns = [

]

urlpatterns += routers.urls