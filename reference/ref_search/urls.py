from django.urls import path
from . import views

app_name = 'ref_search'
urlpatterns = [
    path('search/', views.search, name = "search"),
    path('search_list/', views.ListViewData, name = "search_list"),
    # path('search_list/', views.search_list, name = "search_list"),
]