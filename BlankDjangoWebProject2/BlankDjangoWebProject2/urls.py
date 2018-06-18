"""
Definition of urls for BlankDjangoWebProject2.
"""

from django.conf.urls import include, url
import HelloDjangoApp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', BlankDjangoWebProject2.views.home, name='home'),
    # url(r'^BlankDjangoWebProject2/', include('BlankDjangoWebProject2.BlankDjangoWebProject2.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),
    url(r'^about$', HelloDjangoApp.views.about, name='about'),
    url(r'^getRoles$', HelloDjangoApp.views.getRoles, name='getRoles'),
]
