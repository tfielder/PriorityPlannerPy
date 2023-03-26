from django.contrib import admin
from .models import CollectionItem, ItemCollection

admin.site.register(ItemCollection)
admin.site.register(CollectionItem)
