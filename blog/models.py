from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(u'标签', max_length=20)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        return self.tag_name


class Classification(models.Model):
    name = models.CharField(u'文章分类', max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(u'作者', max_length=30)
    email = models.EmailField(u'邮箱', blank=True)
    website = models.URLField(u'网站', blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    caption = models.CharField(u'标题', max_length=30)
    subcaption = models.CharField(u'小标题', max_length=50, blank=True)
    description = models.TextField(u'摘要', max_length=300)
    publish_time = models.DateTimeField(u'发布时间', auto_now_add=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True)
    author = models.ForeignKey(Author)
    classification = models.ForeignKey(Classification)
    tags = models.ManyToManyField(Tag, blank=False)
    content = UEditorField(u'内容', width=1000, height=300, toolbars="full", imagePath="/photo2", filePath="", upload_settings={"imageMaxSize":1204000},
             settings={}, command=None, blank=True)

    def __str__(self):
        return self.caption


class Picture(models.Model):
    des = models.CharField(u'描述', max_length=100)
    picture = models.ImageField(u'图片', upload_to='./photo1')
    create_date = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.des
