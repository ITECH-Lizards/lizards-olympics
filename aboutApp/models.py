from django.db import models


# Create your models here.
class Expert(models.Model):  # 荣誉模型
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='description')
    photo = models.ImageField(upload_to='Expert/',
                              blank=True,
                              verbose_name='photo')

    class Meta:
        verbose_name = 'expert'
        verbose_name_plural = 'experts'
