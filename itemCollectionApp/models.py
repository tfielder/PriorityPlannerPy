from django.db import models

class ItemCollection(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class CollectionItem(models.Model):
    title = models.CharField(max_length=100)
    itemCollection = models.ForeignKey(ItemCollection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

