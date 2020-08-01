from django.views import generic

# Create your views here.
class SearchView(generic.TemplateView):
    template_name = "search.html"
search = SearchView.as_view()

class ListView(generic.TemplateView):
    template_name = "search_list.html"
search_list = ListView.as_view()