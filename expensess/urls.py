"""
	家計簿
	URL定義

	FIlename : urls.py
	Date : 2020.3.7
	Written by Nobuharu Shimazu

"""
from django.urls import path, include
from . import views

app_name = "expensess"  #アプリケーション名
urlpatterns = [
	path("",views.expensess_list, name="expensess_list"),
	path("expensess/<int:pk>/", views.expensess_detail, name="expensess_detail"),
	path("accounts/", include("django.contrib.auth.urls")),
	path("expensess/add/",views.ExpensessCreateView.as_view(),name="expensess_add"),

]