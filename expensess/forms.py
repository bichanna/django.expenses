"""
	家計簿アプリ
	フォームクラス

	Filename  forms.py
	Date: 2020,5,18
	Written by Nobuharu Shimazu
"""

from django.forms import ModelForm
from django import forms
from .models import Expensess

class ExpensessForm(ModelForm):
	"""
		金額追加画面用のフォーム
		number : 順番
		date : 日付
		category : カテゴリー
		cost : 金額
		memo : メモ
	"""
	class Meta:
		#モデルクラスを指定
		model = Expensess
		#モデルフィールドを指定
		fields = ("number","date","category","cost","memo")
		labels = {
			"number": "順番",
			"date": "日付",
			"category": "カテゴリー",
			"cost": "コスト",
			"memo": "メモ",
		}


class ExpensessSearchForm(forms.Form):
	"""
		表検索用のフォーム
	"""
	key_word = forms.CharField(label="検索キーワード",required=False)