from django.shortcuts import render
from django.views import generic
from .models import ReferenceData
import logging

# Create your views here.
# search.htmlの表示
class SearchView(generic.TemplateView):
    template_name = "search.html"
search = SearchView.as_view()

# def search_title(request):
#     if request.method == "POST":
#         instance_title = ReferenceData().title
#         title = MemberModelForm(request.POST, instance=instance_title)
#         title.save()
#         return redirect(to="search_list.html")
#     else:
#         return HttpResponse("検索ワードを入力してください")

# 検索結果の出力
# class ListView(generic.TemplateView):
#     template_name = "search_list.html"
# search_list = ListView.as_view()

logger = logging.getLogger(__name__)
def ListViewData(request, *args, **kwargs):
    pre_title = request.POST.get('title', False)
    data = {
        'references':ReferenceData.objects.all().filter(title__contains=pre_title),
    }
    return render(request, "search_list.html", data)

