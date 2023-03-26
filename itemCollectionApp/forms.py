from django import forms
from .models import ItemCollection

class ItemCollectionForm(forms.ModelForm):

    class Meta:
        model = ItemCollection

        fields = [
            "title",
            "description"
        ]