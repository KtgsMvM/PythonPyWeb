from django.contrib import admin
from .models import Author, Tag, Entry, AuthorProfile

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Entry)
admin.site.register(AuthorProfile)

# Зарегистрируйте свои модели в админ панели здесь
