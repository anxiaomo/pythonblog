import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythonblog.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''


if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from hello.models import Person
    f = open('person.txt')

    personlist = [Person(name=line.split(' ')[0], age=line.split(' ')[1], sex=line.split(' ')[2]) for line in f]

    Person.objects.bulk_create(personlist)

if __name__ == "__main__":
    main()
    print('Done!')
