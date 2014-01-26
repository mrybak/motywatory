from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.decorators import login_required
from motywatory.views import AddView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'motywatory.views.index', name='index'),
    url(r'^get_motivators/(?P<from_no>\d+)/(?P<to_no>\d+)$', 'motywatory.views.get_motivators', name='get_motivators'),
    url(r'^add$', login_required(AddView.as_view()), name='add'),
    url(r'^add-motivator/$', 'motywatory.views.add_motivator'),

    url(r'^search/', include('haystack.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^update-user/$', 'motywatory.views.update_user', name='update-user'),

     url(r'^images/(?P<path>.*)/$', 'motywatory.views.show_image', name='show_image'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
