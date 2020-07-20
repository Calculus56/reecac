from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):

    priority = 0.6

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


class StaticViewContact(Sitemap):

    priority = 0.6

    def items(self):
        return ['contact']

    def location(self, item):
        return reverse(item)


class StaticViewPolicy(Sitemap):

    priority = 0.6

    def items(self):
        return ['policy']

    def location(self, item):
        return reverse(item)


class StaticViewTeam(Sitemap):

    priority = 0.6

    def items(self):
        return ['team']

    def location(self, item):
        return reverse(item)


class StaticViewAbout(Sitemap):

    priority = 0.6

    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)