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
from .forms import ExpensessForm, ExpensessSearchForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

"""
class ExpensessListView(View):
	def get(self,request,*args,**kwargs):
			#Get request用の処理
			#家計簿一覧を表示する
		context = {}
		expensess = Expensess.objects.all()
		context["expensess"] = expensess
		return render(request,"expensess/expensess_list.html",context)

expensess_list = ExpensessListView.as_view()


class ExpensessDetailView(DetailView):  #大文字を全て小文字にして使える。
	model = Expensess
	template_name = "expensess/expensess_detail.html"

expensess_detail = ExpensessDetailView.as_view()


"""


class ExpensessListView(ListView):
	
		#Get request用の処理
		#表一覧を表示する。
	
	model = Expensess
	template_name = "expensess/expensess_list.html"
	paginate_by = 6

	def get_queryset(self):
		
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
		print("*********")
		print(queryset)
		print("********")
		return queryset

	
	def get_context_data(self, **kwargs):
		
			#コンテキストの設定
		context = super().get_context_data(**kwargs)
		context["form"] = self.form
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


#<td><a href="{% url 'expensess:expensess_detail' pk=expense.pk %}">{{ expense.number }}</a></td>
#<td data-href="/kakeibo/{{expense.id}}/">{{ expense.number }}</td>
#<script src="/static/js/clicktable.js"></script>
#data-href="{% url 'expensess:expensess_detail' pk=expense.pk %}"
#data-href="/expensess/{{pk=expense.pk}/"



