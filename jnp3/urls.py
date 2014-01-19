from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'motywatory.views.index', name='index'),
    url(r'^add$', 'motywatory.views.add', name='add'),
    # url(r'^jnp3/', include('jnp3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
