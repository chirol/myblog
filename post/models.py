from django.db import models

# Create your models here.
class Tags(models.Model):
    tags = models.CharField('タグ名', max_length=140)

    def __str__(self):
        return self.tags


class Category(models.Model):
    Category = models.CharField('カテゴリ名', max_length=30)

    def __str__(self):
        return self.Category


class Post(models.Model):
    tags = models.ManyToManyField(Tags, verbose_name='タグ')
    categories = models.ManyToManyField(Category, verbose_name='カテゴリ')
    title = models.CharField('タイトル', max_length=140)
    date = models.DateField('追加日時')
    body = models.TextField('本文')

    def __str__(self):
        return self.title
