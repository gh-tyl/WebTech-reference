from django.views import generic

# Create your views here.
class SearchView(generic.TemplateView): #LoginRequiredMixinを先に
    template_name = "search.html"
search = SearchView.as_view()