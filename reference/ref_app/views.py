from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(LoginRequiredMixin, generic.TemplateView): #LoginRequiredMixinを先に
    template_name = "index.html"
    #403を出して明示的にしたければ下記を使用
    #raise_exception = True
index = IndexView.as_view()