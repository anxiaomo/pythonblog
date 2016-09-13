from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Person
from django.views.decorators.cache import cache_page
import qrcode


def index(request):
    return HttpResponse("欢迎光临 自强学堂!")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))


# @cache_page(60 * 15)
def home(request):
    # p = Person(name="WZ", age=23)
    # p.save()
    persons= Person.objects.all()
    return render(request, 'index.html', {'persons': persons})


