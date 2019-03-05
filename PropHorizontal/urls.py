from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from PropHorizontal.views import PropHorizontalViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'api', PropHorizontalViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls