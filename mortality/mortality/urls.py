from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from actuaries.api.resources import ActuaryViewSet

router = routers.DefaultRouter()
router.register(r'actuaries', ActuaryViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'mortality.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
