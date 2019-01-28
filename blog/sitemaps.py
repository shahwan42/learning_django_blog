from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9  # relevance to website content

    def items(self):  # items of the xml
        return Post.published.all()

    def lastmod(self, obj):  # run on each item returned from items
        return obj.updated  # correspond to updated date for each post
