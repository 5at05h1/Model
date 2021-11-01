import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students, Person

# all
# print(Students.objects.all())

# IN
ids = [13, 14, 15]
# print(Students.objects.filter(pk__in=ids))

# contain 部分一致
# like '%~~%'
# print(Students.objects.filter(name__contains='三'))

# is null
# p = Person(
#     first_name='Jiro', last_name='Yamada',
#     birthday='2000-01-01', email='aa@mail.com',
#     salary=None, memo='memo jiro', web_site='http://jiro.com'
# )
# p.save()

# filter 指定した条件、exclude: 指定した条件以外
# isnull: Nullのもの
# print(Person.objects.filter(salary__isnull=True))
# print(Person.objects.exclude(salary__isnull=True))

# print(Students.objects.exclude(name='太郎'))

# values: 一部のカラムのみ取り出す
print(Students.objects.values('name', 'age').filter(pk=14).query)

students = Students.objects.values('id', 'name', 'age')
for student in students:
    print(student['id'])

# 並び替え
# : 昇順, -: 降順, (,): 複数
print(Students.objects.order_by('-name', 'id'))