from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
url(r'^admin/', include(admin.site.urls)),
url(r'^$', 'arena_reconstruction.views.home', name = 'home'),
url(r'^course(?P<number>\d+)/$', 'arena_reconstruction.views.course', name='course'),
url(r'^final/$', 'arena_reconstruction.views.final', name ='final'),
url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
url(r'^logout/$', 'django.contrib.auth.views.logout', 
                          {'next_page': '/successfully_logged_out/'}, name='logout'),
url(r'^successfully_logged_out/$', 'arena_reconstruction.views.successfully_logged_out', name='successfully_logged_out'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)