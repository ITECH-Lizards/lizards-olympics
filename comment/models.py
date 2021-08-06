import datetime

from django.conf import settings
from django.db import models

from newsApp.models import MyNew

class CommentQuerySet(models.query.QuerySet):

    def get_count(self):
        return self.count()

    def get_today_count(self):
        return self.exclude(timestamp__lt=datetime.date.today()).count()

class Comment2(models.Model):
    list_display = ("content","timestamp",)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30,blank=True, null=True)
    avatar = models.CharField(max_length=100,blank=True, null=True)
    news = models.ForeignKey(MyNew, on_delete=models.CASCADE,default=1)
    content = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = CommentQuerySet.as_manager()

    class Meta:
        db_table = "n_comment"
        verbose_name = "评论"
        verbose_name_plural = verbose_name