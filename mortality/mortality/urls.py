from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'mortal2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^actuaries/', include('actuaries.api.urls')),
]
