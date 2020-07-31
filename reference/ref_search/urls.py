from django.urls import path
from . import views

app_name = 'ref_search'
urlpatterns = [
    path('search/', views.search, name = "search"),
]

