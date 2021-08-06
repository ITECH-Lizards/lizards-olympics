from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone
from django.conf import settings
# Create your models here.


class MyNew(models.Model):
    NEWS_CHOICES = (
        ('企业要闻', '企业要闻'),
        ('行业新闻', '行业新闻'),
        ('通知公告', '通知公告'),
    )
    title = models.CharField(max_length=50, verbose_name=' 新闻标题')
    description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='news/images/',
                               filePath='news/files/')
    newType = models.CharField(choices=NEWS_CHOICES,
                               max_length=50,
                               verbose_name='新闻类型')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)
    photo = models.ImageField(upload_to='news/',
                              blank=True,
                              null=True,
                              verbose_name='展报')

    liked = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   blank=True, related_name="liked_news")
    collected = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       blank=True, related_name="collected_news")
    def __str__(self):
        return self.title
    def switch_like(self, user):
        if user in self.liked.all():
            self.liked.remove(user)
        else:
            self.liked.add(user)

    def count_likers(self):
        return self.liked.count()

    def user_liked(self, user):
        if user in self.liked.all():
            return 0
        else:
            return 1

    def switch_collect(self, user):
        if user in self.collected.all():
            self.collected.remove(user)

        else:
            self.collected.add(user)

    def count_collecters(self):
        return self.collected.count()

    def user_collected(self, user):
        if user in self.collected.all():
            return 0
        else:
            return 1

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "新闻"
        verbose_name_plural = verbose_name