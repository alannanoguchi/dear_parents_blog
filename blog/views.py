from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from blog.models import Page
from blog.forms import PageForm


class PostListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PostDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific blog page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })


class PostCreateView(CreateView):

  model = Page
 
  def get(self, request, *args, **kwargs):
    context = {'form': PageForm()}
    return render(request, 'new_page.html', context)

  def post(self, request, *args, **kwargs):
    form = PageForm(request.POST)
    if form.is_valid():
      page = form.save()
      return HttpResponseRedirect(reverse_lazy('blog-list-page')) # when the page is saved, you'll be rerouted back to the wiki list page
    return render(request, 'new_page.html', {'form': form})
