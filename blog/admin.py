from django.contrib import admin
from .models import Article, Classification, Tag, Author, Picture


admin.site.register(Article)
admin.site.register(Classification)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Picture)
