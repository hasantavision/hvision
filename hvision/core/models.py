from djongo import models

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_slug = models.CharField(max_length=200, default='')
    article_pub_date = models.DateTimeField('published')
    article_description = models.TextField(max_length=500, default='')
    article_body = models.TextField(max_length=10000, default='')
    article_author = models.TextField()
