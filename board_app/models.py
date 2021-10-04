from django.db import models

# Create your models here.
class Board(models.Model):
    author = models.CharField(max_length=10, null=False)
    keyword = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class Keyword(models.Model):
    keyword = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=255, null=False)
    writeData = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    reply = models.CharField(max_length=255, null=False)
    replyList = models.TextField(null=True)
    like = models.CharField(max_length=255, null=False)
    user_name = models.CharField(max_length=255, null=False)
    user_pk = models.CharField(max_length=255, null=False)
    user_id = models.CharField(max_length=255, null=False)