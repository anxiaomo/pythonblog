from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(u'姓名', max_length=30)
    age = models.IntegerField(u'年龄')
    sex = models.IntegerField(u'性别')
    content = models.TextField(u'内容')

    def __str__(self):
        return self.name

