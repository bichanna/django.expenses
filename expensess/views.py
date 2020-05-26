from django.shortcuts import render, reverse

# Create your views here.
"""
	家計簿
	表示用の機能作成

	File name : views.py
	Date : 2020.3.7
	Written by Nobuharu Shimazu

"""
from django.views.generic import View,DetailView, CreateView
from django.utils import timezone
from .models import Expensess,Category
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


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


class ExpensessDetailView(DetailView):  #大文字を全て小文字にして使える。
	model = Expensess
	template_name = "expensess/expensess_detail.html"

expensess_detail = ExpensessDetailView.as_view()


class ExpensessCreateView(LoginRequiredMixin, CreateView):
	"""
		金額追加ページ作成用のビュー
	"""
	model = Expensess
	form_class = PostForm
	template_name = "expensess/expensess_add.html"

	def form_valid(self, form):
		form.instance.author = self.request.user

		return super().form_valid(form)


	def get_success_url(self):
		"""詳細画面にリダイレクトする。"""
		return reverse("expensess:expensess_detail",args=(self.object.id,))
















"""
class CategoryListView(View):
	def get(self,request,*args,**kwargs):
		context = {}
		category = Category.objects.all()
		context["category"] = category
		return render(request,"expensess/expensess_list.html",context)
"""