from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog Posts"
    link = "/feed/"
    description = "Latest blog posts."

    def items(self):
        print("IN ITEMS")
        return Post.objects.all().order_by('-published_date')[:5]

    def item_title(self, item):
        print("IN TITLE")
        return item.title

    def item_description(self, item):
        print("IN DESCRIPTION")
        return item.text

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        print(item.pk)
        return reverse('blog_detail', args=[item.pk])
