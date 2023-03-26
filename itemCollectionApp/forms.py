from django import forms
from .models import CollectionItem, ItemCollection

class ItemCollectionForm(forms.ModelForm):

    class Meta:
        model = ItemCollection

        fields = [
            "title",
            "description"
        ]


class CollectionItemForm(forms.ModelForm):

    class Meta:
        model = CollectionItem
        exclude = ('itemCollection',)

        fields = [
            "title",
            "description"
        ]