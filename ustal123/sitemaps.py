from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return ['index']  # имя маршрута главной страницы

    def location(self, item):
        return reverse(item)
