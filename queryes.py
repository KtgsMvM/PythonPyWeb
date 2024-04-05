import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)
obj = Entry.objects.filter(author__name__contains='author')
print(obj)
"""<QuerySet [<Entry: Оазисы Сахары: красота и опасность>, 
<Entry: Новые гаджеты и устройства: обзор рынка>]>"""

obj = Entry.objects.filter(author__authorprofile__city=None)
print(obj)
"""<QuerySet [<Entry: Знакомство с Парижем>, 
<Entry: Инновации в области виртуальной реальности>]>"""
print(Entry.objects.get(id__exact=4))
print(Entry.objects.get(id=4))  # Аналогично exact
print(Blog.objects.get(name__iexact="Путешествия по миру")

print(Entry.objects.filter(headline__contains='мод'))
# <QuerySet [
# <Entry: Тенденции моды на текущий сезон>,
# <Entry: История моды: от ретро до современности>,
# <Entry: Интервью с известными модельерами и дизайнерами>
# ]>
print(Entry.objects.filter(id__in=[1, 3, 4]))
# <QuerySet [<Entry: Изучение красот Мачу-Пикчу>, <Entry: Знакомство с Парижем>, <Entry: Открывая тайны Колизея>]>

print(Entry.objects.filter(number_of_comments__in='123'))  # число комментариев 1 или 2 или 3
"""
<QuerySet [
<Entry: Изучение красот Мачу-Пикчу>, 
<Entry: Открывая тайны Колизея>, 
<Entry: Экзотические специи и их использование>, 
<Entry: Упражнения для поддержания физической формы>, 
<Entry: Топ-10 фитнес-тренеров для вдохновения>, 
<Entry: История моды: от ретро до современности>
]>
"""
inner_qs = Blog.objects.filter(name__contains='Путешествия')
entries = Entry.objects.filter(blog__in=inner_qs)
print(entries)
"""
<QuerySet [
<Entry: Изучение красот Мачу-Пикчу>, 
<Entry: Приключения в Амазонке>, 
<Entry: Знакомство с Парижем>, 
<Entry: Открывая тайны Колизея>, 
<Entry: Оазисы Сахары: красота и опасность>
]>
"""
# Вывести все записи, у которых число комментарием больше 10
print(Entry.objects.filter(number_of_comments__gt=10))
"""
<QuerySet [
<Entry: Приключения в Амазонке>, 
<Entry: Новые гаджеты и устройства: обзор рынка>, 
<Entry: Кибербезопасность: защита вашей конфиденциальности>, 
<Entry: Инновации в области виртуальной реальности>
]>
"""
# Вывести все записи, которые опубликованы (поле pub_date) позже и равное 01.06.2023
import datetime
print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
"""
<QuerySet [
<Entry: Приготовление собственного хлеба>, 
<Entry: Десерты для настоящих сладкоежек>, 
<Entry: Упражнения для поддержания физической формы>, 
<Entry: Топ-10 фитнес-тренеров для вдохновения>, 
<Entry: Как правильно заниматься йогой>, 
<Entry: Последние тренды в мире искусственного интеллекта>, 
<Entry: Как создать стильный образ на каждый день>, 
<Entry: История моды: от ретро до современности>
]>
"""
# Вывести все записи, у которых число комментарием больше 10 и рейтинг < 4
print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
"""
<QuerySet [
<Entry: Новые гаджеты и устройства: обзор рынка>, 
<Entry: Кибербезопасность: защита вашей конфиденциальности>
]>
"""
# Вывести все записи, у которых заголовок статьи лексиграфически <= "Зя"
print(Entry.objects.filter(headline__lte="Зя"))
"""
<QuerySet [
<Entry: Знакомство с Парижем>, 
<Entry: Десерты для настоящих сладкоежек>, 
<Entry: Гастрономическое путешествие по Франции>, 
<Entry: Здоровое питание: полезные рецепты>
]>
"""
print(Entry.objects.filter(headline__startswith='Как'))
# <QuerySet [<Entry: Как правильно заниматься йогой>, <Entry: Как создать стильный образ на каждый день>]>
print(Entry.objects.filter(headline__endswith='ния'))
# <QuerySet [<Entry: Топ-10 фитнес-тренеров для вдохновения>, <Entry: Секреты успешного похудения>]>

# Вывести записи между 01.01.2023 и 31.12.2023
import datetime
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)
print(Entry.objects.filter(pub_date__range=(start_date, end_date)))
"""
<QuerySet [
<Entry: Оазисы Сахары: красота и опасность>, 
<Entry: Рецепты блюд из итальянской кухни>, 
<Entry: Приготовление собственного хлеба>, 
<Entry: Десерты для настоящих сладкоежек>, 
<Entry: Гастрономическое путешествие по Франции>, 
<Entry: Упражнения для поддержания физической формы>, 
<Entry: Здоровое питание: полезные рецепты>, 
<Entry: Секреты успешного похудения>, 
<Entry: История моды: от ретро до современности>, 
<Entry: Уход за кожей и волосами: лучшие советы>, 
<Entry: Интервью с известными модельерами и дизайнерами>
]>
"""
# При данной постановке задачи (вывод за конкретный год) будет проще воспользоваться __year результат будет аналогичен
print(Entry.objects.filter(pub_date__year=2023))

# Вывести записи старше 2022 года
print(Entry.objects.filter(pub_date__year__lt=2022))
"""
<QuerySet [
<Entry: Новые гаджеты и устройства: обзор рынка>, 
<Entry: Кибербезопасность: защита вашей конфиденциальности>, 
<Entry: Инновации в области виртуальной реальности>
]>
"""
# Вывести все записи за февраль доступных годов, отобразить название, дату публикации, заголовок
print(Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline'))
"""
<QuerySet [
{'blog__name': 'ИТ-новости и технологии', 'pub_date': datetime.date(2022, 2, 1), 'headline': 'Развитие интернета вещей: будущее или реальность?'}, 
{'blog__name': 'Мода и стиль', 'pub_date': datetime.date(2023, 2, 1), 'headline': 'Уход за кожей и волосами: лучшие советы'}, 
{'blog__name': 'Мода и стиль', 'pub_date': datetime.date(2023, 2, 1), 'headline': 'Интервью с известными модельерами и дизайнерами'}
]>
"""
# Вывести username авторов у которых есть публикации с 1 по 15 апреля 2023 года, вывести без использования range. Пример для работы с __day
print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(pub_date__day__lte=15).values_list("author__name").distinct())
# Сначала отфильтровываем по году, затем по дням, затем получаем значения имен у авторов и говорим, чтобы не было повторов
"""
<QuerySet [
('andrey_author',), 
('dmitriy_creative',), 
('alexander89',), 
('irina_blogger',), 
('ivan_wordsmith',), 
('maxim_writer',)
]>
"""
# Вывести статьи опубликованные в понедельник (так как datetime работает по американской системе,
# то начало недели идёт с воскресенья, а заканчивается субботой, поэтому понедельник второй день в неделе)
print(Entry.objects.filter(pub_date__week_day=2).values('blog__name', 'pub_date', 'headline'))
"""
<QuerySet [
{'blog__name': 'Путешествия по миру', 'pub_date': datetime.date(2022, 8, 1), 'headline': 'Приключения в Амазонке'}, 
{'blog__name': 'Фитнес и здоровый образ жизни', 'pub_date': datetime.date(2023, 5, 1), 'headline': 'Здоровое питание: полезные рецепты'}, 
{'blog__name': 'Фитнес и здоровый образ жизни', 'pub_date': datetime.date(2024, 1, 1), 'headline': 'Топ-10 фитнес-тренеров для вдохновения'}, 
{'blog__name': 'Фитнес и здоровый образ жизни', 'pub_date': datetime.date(2024, 4, 1), 'headline': 'Как правильно заниматься йогой'}, 
{'blog__name': 'ИТ-новости и технологии', 'pub_date': datetime.date(2024, 4, 1), 'headline': 'Последние тренды в мире искусственного интеллекта'}
]>
"""
# week, quarter, hour, minute, second рассматривается аналогично как и всё что было ранее
import datetime
# Вывод всех записей по конкретной дате
print(Entry.objects.filter(pub_date__date=datetime.date(2021, 6, 1)))
# <QuerySet [<Entry: Новые гаджеты и устройства: обзор рынка>]>

# Вывод всех записей новее конкретной даты
print(Entry.objects.filter(pub_date__date__gt=datetime.date(2024, 1, 1)))
"""
<QuerySet [
<Entry: Как правильно заниматься йогой>, 
<Entry: Последние тренды в мире искусственного интеллекта>, 
<Entry: Как создать стильный образ на каждый день>
]>
"""

# Вывод записей по конкретному времени
print(Entry.objects.filter(pub_date__time=datetime.time(12, 00)))
"""
<QuerySet [
<Entry: Как создать стильный образ на каждый день>, 
<Entry: История моды: от ретро до современности>, 
<Entry: Уход за кожей и волосами: лучшие советы>, <Entry: Интервью с известными модельерами и дизайнерами>
]>
"""

# Вывод записей по временному диапазону с 6 утра до 17 вечера
print(Entry.objects.filter(pub_date__time__range=(datetime.time(6), datetime.time(17))))
"""
<QuerySet [
<Entry: Как правильно заниматься йогой>, 
<Entry: Секреты успешного похудения>, 
<Entry: Последние тренды в мире искусственного интеллекта>, 
<Entry: Развитие интернета вещей: будущее или реальность?>, 
<Entry: Новые гаджеты и устройства: обзор рынка>, 
<Entry: Кибербезопасность: защита вашей конфиденциальности>, 
<Entry: Инновации в области виртуальной реальности>, 
<Entry: Тенденции моды на текущий сезон>, 
<Entry: Как создать стильный образ на каждый день>, 
<Entry: История моды: от ретро до современности>, 
<Entry: Уход за кожей и волосами: лучшие советы>, 
<Entry: Интервью с известными модельерами и дизайнерами>]>
"""
# Вывести всех авторов которые не указали город
print(AuthorProfile.objects.filter(city__isnull=True))
"""
<QuerySet [
<AuthorProfile: anna_journey>, 
<AuthorProfile: natalia_author>, 
<AuthorProfile: vladimir_writer>, 
<AuthorProfile: alexandra_creative>, 
<AuthorProfile: svetlana_writer>, 
<AuthorProfile: larisa_thinker>
]>
"""
# Вывести записи где в тексте статьи встречается патерн \w*стран\w*
print(Entry.objects.filter(body_text__regex=r'\w*стран\w*'))
"""
<QuerySet [
<Entry: Гастрономическое путешествие по Франции>, 
<Entry: Кибербезопасность: защита вашей конфиденциальности>
]>
"""
# Вывести записи авторов с почтовыми доменами @gmail.com и @mail.ru
print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)'))
"""
<QuerySet [
<Entry: Изучение красот Мачу-Пикчу>, 
<Entry: Знакомство с Парижем>, 
<Entry: Приготовление собственного хлеба>, 
<Entry: Гастрономическое путешествие по Франции>, 
<Entry: Упражнения для поддержания физической формы>, 
<Entry: Кибербезопасность: защита вашей конфиденциальности>, 
<Entry: Инновации в области виртуальной реальности>, 
<Entry: Как создать стильный образ на каждый день>, 
<Entry: Уход за кожей и волосами: лучшие советы>, 
<Entry: Интервью с известными модельерами и дизайнерами>
]>
"""
# Если необходимо вывести записи авторов с почтовыми доменами @gmail.com и @mail.ru, но чтобы значения не повторялись, то используем distinct()
print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)').distinct())
"""
<QuerySet [
<Entry: Изучение красот Мачу-Пикчу>, 
<Entry: Знакомство с Парижем>, 
<Entry: Приготовление собственного хлеба>, 
<Entry: Гастрономическое путешествие по Франции>, 
<Entry: Упражнения для поддержания физической формы>, 
<Entry: Кибербезопасность: защита вашей конфиденциальности>, 
<Entry: Инновации в области виртуальной реальности>, 
<Entry: Как создать стильный образ на каждый день>, 
<Entry: Уход за кожей и волосами: лучшие советы>, 
<Entry: Интервью с известными модельерами и дизайнерами>
]>
"""
all_obj = Blog.objects.all()
print("Вывод всех значений в таблице Blog\n", all_obj)

all_obj = Blog.objects.first()
print("Вывод первого значения в таблице Blog\n", all_obj)

all_obj = Blog.objects.all()
obj_first = all_obj.first()
print("Разные запросы на вывод в Blog\n", f"Первое значение таблицы = {obj_first}\n",
       f"Все значения = {all_obj}")

all_obj = Blog.objects.all()
for idx, value in enumerate(all_obj):
    print(f"idx = {idx}, value = {value}")
print(all_obj[0])  # Получение 0-го элемента
print(all_obj[2:4])  # Получение 2 и 3 элемента
"""Получение последнего элемента не осуществимо через обратный индекс
all_obj[-1] - нельзя
можно воспользоваться latest('<name_field>'), где <name_field> - имя колонки в БД.

Почти все операции над БД не требуют предварительного получения всех элементов, постоянная запись Blog.objects.all()
просто для примера.
"""
print(all_obj.latest("id"))  # Получение последнего элемента
print(Blog.objects.latest("id"))  # Одинаково работает

# Пример получения элемента по одному условию
print(Blog.objects.get(id=1))
# Пример получения элемента по двум условиям. Условия работают с оператором И, т.е. выведется строка, только с
# совпадением и первого и второго параметра.
print(Blog.objects.get(id=1, name="Путешествия по миру"))
# Если нет совпадений, то выйдет исключение "db.models.Blog.DoesNotExist: Blog matching query does not exist."
print(Blog.objects.get(id=2, name="Путешествия по миру"))


print(Blog.objects.filter(id__gte=2))  # Вывод всех строк таблицы Blog у которых значение id >= 2.
# Рассмотрение поиска по полям далее

print(Blog.objects.exclude(id__gte=2))  # Вывод всех строк таблицы Blog кроме тех у которых значение id >= 2.
#  <QuerySet [<Blog: Путешествия по миру>]>

# Пример для get
try:
    Blog.objects.get(id=2, name="Путешествия по миру")
except Blog.DoesNotExist:
    print("Не существует")
# Пример для filter
print(Blog.objects.filter(id=2, name="Путешествия по миру").exists())

print(Blog.objects.count())  # Можно ко всей таблице
print(Blog.objects.filter(id__gte=2).count())  # Можно к запросу
all_data = Blog.objects.all()
filtred_data = all_data.filter(id__gte=2)
print(filtred_data.count())  # Можно к частным запросам

filtered_data = Blog.objects.filter(id__gte=2)
print(filtered_data.order_by("id"))  # упорядочивание по возрастанию по полю id
print(filtered_data.order_by("-id"))  # упорядочивание по уменьшению по полю id
print(filtered_data.order_by("-name", "id"))  # упорядочивание по двум параметрам, сначала по первому на уменьшение,
# затем второе на увеличение. Можно упорядочивание провести по сколь угодно параметрам.


from django.db.models import Count
# Запрос, аннотирующий количество статей для каждого блога,
# при этом добавляется новая колонка number_of_entries для вывода
entry = Blog.objects.annotate(number_of_entries=Count('entries')).values('name', 'number_of_entries')
print(entry)
"""
<QuerySet [
{'name': 'Путешествия по миру', 'number_of_entries': 5}, 
{'name': 'Кулинарные искушения', 'number_of_entries': 5}, 
{'name': 'Фитнес и здоровый образ жизни', 'number_of_entries': 5}, 
{'name': 'ИТ-новости и технологии', 'number_of_entries': 5}, 
{'name': 'Мода и стиль', 'number_of_entries': 5}
]>
"""


from django.db.models import Count
blogs = Blog.objects.alias(number_of_entries=Count('entries')).filter(number_of_entries__gt=4)
print(blogs)
"""
<QuerySet [
<Blog: Путешествия по миру>, 
<Blog: Кулинарные искушения>, 
<Blog: Фитнес и здоровый образ жизни>, 
<Blog: ИТ-новости и технологии>, 
<Blog: Мода и стиль>
]>
"""

## Выведет ошибку, так как поле number_of_entries не существует, виду различий между alias и annotate
# blogs = Blog.objects.alias(number_of_entries_new=Count('entries')).filter(number_of_entries__gt=4).values('blog', 'entries_new')
from django.db.models import Avg, Q

# Вычислить среднюю оценку только для уникальных значений
average_rating = Entry.objects.aggregate(
    average_rating1=Avg('rating', distinct=True)
)
print(average_rating)  # {'average_rating1': 3.6999999999999993}

# Вычислить среднюю оценку с заданным значением по умолчанию(допустим
# значение у поля None), если агрегация не возвращает результат
average_rating_with_default = Entry.objects.aggregate(
    average_rating2=Avg('rating', default=5.0)
)
print(average_rating_with_default) # {'average_rating2': 3.46}

# Вычислить среднюю оценку только для статей, опубликованных после 2023 года
average_rating = Entry.objects.aggregate(
    average_rating3=Avg('rating', filter=Q(pub_date__year__gt=2023)))
print(average_rating) # {'average_rating3': 2.925}