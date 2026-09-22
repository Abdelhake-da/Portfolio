"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from portfolio import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.decorators.cache import cache_control
from app.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', cache_control(max_age=2592000, public=True)(serve), {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', cache_control(max_age=2592000, public=True)(serve), {'document_root': settings.STATIC_ROOT}),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

handler404 = 'app.views.custom_404'
if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += [
    ]+debug_toolbar_urls()
