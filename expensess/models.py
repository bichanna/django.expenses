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

class Expensess(models.Model):
	"""
		家計簿

		author  : 作者(Djangoのユーザーを使用)
		title  : タイトル
		category_ID: カテゴリーのID
		category name: カテゴリー名
		cost: 金額
		number: 順番番号
		date : 日付
		memo : メモ
	"""

	#フィールドの定義
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	#                                     ↑ここの説明をしてもらう
	#category_ID = models.ForeignKey(settings.)
	title = models.CharField(max_length=200)
	#category_ID = models.TextField()
	category = models.TextField()
	cost = models.TextField()
	number = models.TextField()
	memo = models.TextField()
	date = models.DateTimeField(blank=True, null=True)


	def __str__(self):
		return self.title
