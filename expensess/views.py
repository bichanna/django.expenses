from django.shortcuts import render

# Create your views here.
"""
	家計簿
	表示用の機能作成

	File name : views.py
	Date : 2020.3.7
	Written by Nobuharu Shimazu

"""
from django.views.generic import View
from django.utils import timezone
from .models import Expensess


class ExpensessListView(View):
	def get(self,request,*args,**kwargs):
		"""
			Get request用の処理
			家計簿一覧を表示する
		"""
		context = {}
		expensess = Expensess.objects.all()
		context["expensess"] = expensess
		return render(request,"expensess/expensess_list.html",context)

expensess_list = ExpensessListView.as_view()