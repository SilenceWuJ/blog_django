from django.db import models

# Create your models here.
"""
models.py中的一个类就对应数据库中的一张表，类中的一个对象就对应表中的一个字段
"""
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    abstract = models.TextField()
    content = models.TextField()
    class Meta:
        db_table = "blog_info"
class Users(models.Model):
    user_name = models.CharField(max_length = 20)
    user_password = models.CharField(max_length = 20)
    class Meta:
        db_table = "user_indo"




