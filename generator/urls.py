from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('export_txt/', views.export_txt, name='export_txt'),
    path('get/', views.results, name='results'), # 追加する
]
