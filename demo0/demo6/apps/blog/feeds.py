from django.contrib.syndication.views import Feed
from  .models import Artical
class ArticalFeed(Feed):
    title="yyx的博客"
    description = "介绍一些开发知识"
    link="/"
    def items(self):
        return Artical.objects.order_by("-createtime")[:5]
    def item_link(self, item):
        pass

