from django.db import models

# Create your models here.
"""
	家計簿
	データモデル

	Filename  models.py
	Date: 2020.3.5
	Written by Nobuharu Shimazu
"""
from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
	#フィールドの定義
	category = models.TextField()

	def __str__(self):
		return self.category






class Expensess(models.Model):
	"""
		家計簿

		author  : 作者(Djangoのユーザーを使用)
		title  : タイトル
		category: カテゴリーのID
		cost: 金額
		number: 順番番号
		date : 日付
		memo : メモ
	"""

	#フィールドの定義
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="カテゴリー")
	title = models.CharField(max_length=200,verbose_name="タイトル")

	cost = models.IntegerField(verbose_name="コスト")
	number = models.IntegerField(verbose_name="順番")
	memo = models.TextField(verbose_name="メモ")
	date = models.DateField(blank=True,null=True,verbose_name="日付")


	def __str__(self):
		return str(self.author) + ":" +str(self.number) + "     " + str(self.id) + "    " + self.title












