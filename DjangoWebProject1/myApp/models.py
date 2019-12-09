"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django import db
# Create your models here.

class Suggestion(models.Model):
    suggestion_title = models.CharField('Название предложения', 
                                        max_length = 100,
                                        null=True)
    suggestion_author = models.CharField('Автор предложения', 
                                         max_length = 12, 
                                         null=False,
                                         blank=False)
    suggestion_text = models.TextField('Текст предложения',
                                       null=True)
    pub_date = models.DateTimeField('Дата публикации')
    verbose_name = 'Предложения'

    def __str__(self):
        return self.suggestion_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

# Comments in suggestion topics
class Comment(models.Model):
    suggestion = models.ForeignKey(Suggestion, on_delete = models.CASCADE)
    comment_author = models.CharField('Автор комментария', 
                                      max_length = 12, 
                                      default = 'None',
                                      null=False,
                                      blank=False)
    comment_text = models.CharField('Текст комментария', 
                                    max_length = 200)
    #pub_date = models.DateTimeField('Дата публикации', default=0)

    def __str__(self):
        return self.comment_author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class News(models.Model):
	news_name = models.CharField(max_length = 1000)
	news_text = models.TextField(default="")
	news_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.news_name