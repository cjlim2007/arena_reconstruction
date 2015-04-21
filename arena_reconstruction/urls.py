from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
url(r'^admin/', include(admin.site.urls)),
url(r'^$', 'arena_reconstruction.views.home', name = 'home'),
url(r'^course1/$', 'arena_reconstruction.views.course1', name='course1'), 
url(r'^course2/$', 'arena_reconstruction.views.course2', name='course2'),
url(r'^course3/$', 'arena_reconstruction.views.course3', name ='course3'),
url(r'^course4/$', 'arena_reconstruction.views.course4', name ='course4'),
url(r'^course5/$', 'arena_reconstruction.views.course5', name ='course5'),
url(r'^course6/$', 'arena_reconstruction.views.course6', name ='course6'),
url(r'^course7/$', 'arena_reconstruction.views.course7', name ='course7'),
url(r'^temp/$', 'arena_reconstruction.views.showClass', name='temp'),
url(r'^final/$', 'arena_reconstruction.views.final', name ='final'),
url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
url(r'^logout/$', 'django.contrib.auth.views.logout', 
                          {'next_page': '/successfully_logged_out/'}, name='logout'),
url(r'^successfully_logged_out/$', 'arena_reconstruction.views.successfully_logged_out', name='successfully_logged_out'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)