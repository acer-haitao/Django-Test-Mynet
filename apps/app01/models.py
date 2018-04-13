from django.db import models

# Create your models here.
class Category(models.Model):
    caption = models.CharField(max_length=32)

class ArticleType(models.Model):
    type = models.CharField(max_length=32)

class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=32)

    category = models.ForeignKey(Category)
    article_type = models.ForeignKey(ArticleType)

