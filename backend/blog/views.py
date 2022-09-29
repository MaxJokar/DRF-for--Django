from django.shortcuts import get_object_or_404

from django.views.generic import DetailView # to show every article separately
from django.views.generic import ListView
from .models import Article


class ArticleList(ListView):
    # get for me a  queryset
    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetail(DetailView):
    # get for me an Object
    def get_object(self):
        # in here we can use get method but some issues like Try : except should be considered to avoide
        # we use the folloing
        return get_object_or_404(
            Article.objects.filter(status=True),
            # kwargs:
            pk=self.kwargs.get("pk")

            )





