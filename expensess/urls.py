"""
	家計簿
	URL定義

	FIlename : urls.py
	Date : 2020.3.7
	Written by Nobuharu Shimazu

"""
from django.urls import path
from . import views

app_name = "expensess"  #アプリケーション名
urlpatterns = [
	path("",views.expensess_list, name="expensess_list"),
]