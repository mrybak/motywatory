from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.decorators import login_required
from motywatory.views import AddView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'motywatory.views.index', name='index'),
    url(r'^add$', login_required(AddView.as_view()), name='add'),
    url(r'^add-motivator/$', 'motywatory.views.add_motivator'),

    url(r'^search/', include('haystack.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^update-user/$', 'motywatory.views.update_user', name='update-user'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
