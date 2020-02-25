from django.shortcuts import render, get_object_or_404


from .models import Article

from .forms import BlogForm

# Create your views here.


def blog_create_view(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogForm() #leeres Formular rendern/laden nach Speichern
    context = {
        "form": form
    }
    return render(request, "blog/article_create.html", context)

def blog_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "blog/article_list.html", context)

def blog_detail_view(request, my_id):
    #obj = Article.objects.get(id=my_id)
    obj = get_object_or_404(Article, id=my_id)

    context = {
        "object": obj
    }
    return render(request, "blog/article_detail.html", context)


#Class-based-Views
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all() #without the line above, the view looks automatically for a template called: <blog>/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    queryset = Article.objects.all()



# Class-based-Views (from methode based views..) siehe 3:24
from django.views import View #BASE VIEW Class = View
