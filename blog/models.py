from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # モデル
    # プロパティ
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 他のモデルへのリンク
    title = models.CharField(max_length=200) # 文字数が制限されたテキストを定義するフィールド
    text = models.TextField() # 制限無しの長いテキスト用
    created_date = models.DateTimeField(default=timezone.now) # 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): # ブログを公開するメソッドそのもの
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title