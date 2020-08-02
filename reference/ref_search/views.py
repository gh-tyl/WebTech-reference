from django.shortcuts import render
from django.views import generic
from .models import ReferenceData

# Create your views here.
class SearchView(generic.TemplateView):
    template_name = "search.html"
search = SearchView.as_view()

# class ListView(generic.TemplateView):
#     template_name = "search_list.html"
# search_list = ListView.as_view()

def ListViewData(request):
    data = {
        'references':ReferenceData.objects.all().filter(title__contains='Qiita'),
    }
    return render(request, "search_list.html", data)