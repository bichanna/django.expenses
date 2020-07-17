from django.shortcuts import render, reverse

# Create your views here.
"""
	家計簿
	表示用の機能作成

	File name : views.py
	Date : 2020.3.7
	Written by Nobuharu Shimazu

"""
from django.views.generic import View,DetailView, CreateView, RedirectView, UpdateView, DeleteView, ListView
from django.utils import timezone
from .models import Expensess,Category
from .forms import ExpensessForm, ExpensessSearchForm, CSVUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import pandas as pd
import numpy as np
from django.views import generic
from django.urls import reverse_lazy
import io


class ExpensessListView(ListView):
	
		#Get request用の処理
		#表一覧を表示する。
	
	model = Expensess
	template_name = "expensess/expensess_list.html"
	paginate_by = 6

	def get_queryset(self):       #テンプレートに送るデータを抽出したいならget_querysetで制限する。
		
			#検索条件の設定
		
		form = ExpensessSearchForm(self.request.GET or None)
		self.form = form

		#フォームが指定したキーワードを取得
		queryset = super().get_queryset()
		if form.is_valid():
			key_word = form.cleaned_data.get("key_word")
			if key_word:
				for word in key_word.split():
					queryset = queryset.filter(Q(number__icontains=word) | Q(category_id__category__icontains=word) | Q(cost__icontains=word) | Q(memo__icontains=word) | Q(date__icontains=word))

		
		queryset = queryset.filter(date__lte=timezone.now()).order_by("date")
		queryset = queryset.filter(author_id__username__icontains=self.request.user.username)
		return queryset

	
	def get_context_data(self, **kwargs):  #テンプレートに辞書を
			#コンテキストの設定
		user = self.request.user.username
		context = super().get_context_data(**kwargs)
		context["form"] = self.form




		"""
		n = 0
		for expense in context["expensess_list"]:
			if self.request.user.is_authenticated:
				if self.request.user.username == expense.author.username:
					n += 1
					#k,v = context["expensess_list"][0].popitem()
					#print("****************************")
					#print(expense)
					#print("****************************")
					#print(context["expensess_list"][0])   #テンプレートでさばいていた情報をこっちに事前にさばく。
					#print("**************************")
		"""
					


		
		
		return context

expensess_list = ExpensessListView.as_view()



class ExpensessDetailView(DetailView):
	model = Expensess
	template_name = "expensess/expensess_detail.html"


expensess_detail = ExpensessDetailView.as_view()






class ExpensessCreateView(LoginRequiredMixin, CreateView):
	"""
		金額追加ページ作成用のビュー
	"""
	model = Expensess
	form_class = ExpensessForm
	template_name = "expensess/expensess_add.html"

	def form_valid(self, form):
		form.instance.author = self.request.user

		return super().form_valid(form)


	def get_success_url(self):
		"""詳細画面にリダイレクトする。"""
		return reverse("expensess:expensess_detail",args=(self.object.id,))


class ExpensessUpdateView(LoginRequiredMixin, UpdateView):
	"""
		変更ページのビュー
	"""
	model = Expensess
	form_class = ExpensessForm
	template_name = "expensess/expensess_update.html"

	def get_success_url(self):
		"""詳細画面にリダイレクトする。"""
		return reverse("expensess:expensess_detail", args=(self.object.id,))


class ExpensessDeleteView(LoginRequiredMixin, DeleteView):
	"""
		削除用のビュー
	"""
	model = Expensess
	template_name = "expensess/expensess_delete.html"
	def get_success_url(self):
		"""一覧ページにリダイレクトする。"""
		return reverse("expensess:expensess_list")



class ExpensessDataImport(LoginRequiredMixin,generic.FormView):
	"""
		データインポート用のビュー
	"""
	#model = Expensess
	success_url = reverse_lazy("expensess:expensess_list")
	template_name = "expensess/expensess_import.html"
	form_class = CSVUpdateForm

	def form_valid(self, form):
		#データの読み込み
		csvfile = form.cleaned_data["file"]
		df = pd.read_csv(csvfile,
						 names = ["title","number","date","category_id","cost","memo","author_id","id"])
		df["date"] = pd.to_datetime(df["date"],format="%Y-%m-%d")
		data_np = np.asarray(df)
		for row in data_np:
			defaults = {
				"title":row[0],
				"number":row[1],
				"date":row[2],
				"category_id":row[3],
				"cost":row[4],
				"memo":row[5],
				"author_id":row[6],
				"id":row[7],
			}
			#print(defaults)

			data, created = Expensess.objects.get_or_create(id=row[7],defaults=defaults)
			#print(str(row[6]) + "*********")
			
			if not created:
				data.title = row[0]
				data.number = row[1]
				data.date = row[2]
				data.category_id = row[3]
				data.cost = row[4]
				print(data.memo)
				print(row[5])
				print(data.title,data.number,data.date,data.category_id,data.cost)
				data.memo = row[5]
				data.author_id = row[6]
				data.id = row[7]
				print(data.memo)
				print("⭐"*20)
				data.save()
		
			


		print("⭐"*10)
		print(form)
		return super().form_valid(form)

	

























