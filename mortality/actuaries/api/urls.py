from django.conf.urls import include, url
from rest_framework import routers
from actuaries.api.resources import ActuaryViewSet

router = routers.DefaultRouter()
router.register(r'actuaries', ActuaryViewSet)

urlpatters = [
    url(r'^', include(router.urls)),
]
