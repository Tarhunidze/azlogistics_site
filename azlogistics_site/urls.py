from django.contrib import admin
from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.views.generic import TemplateView

# Sitemap class
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'projects']

    def location(self, item):
        return reverse(item)

sitemaps = {'static': StaticViewSitemap}

# URL patterns
urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contacts/', include('contacts.urls')),
    path('services/', include('services.urls')),
    path('projects/', include('projects.urls')),
    path('apply/', include('orders.urls')),
    path('yandex_c7fbad4ffccc7f24.html', TemplateView.as_view(template_name="yandex_c7fbad4ffccc7f24.html")),
path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),name='robots'),
    path('googleeeca2c9c57c16fbe.html', TemplateView.as_view(
        template_name="googleeeca2c9c57c16fbe.html",
        content_type="text/html"
    )),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
