from django.shortcuts import render
from django.http import Http404

from .models import CollectionItem, ItemCollection
from .forms import ItemCollectionForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def collections(request):
    itemCollections = ItemCollection.objects.all()

    return render(request, 'collections.html', { 'itemCollections': itemCollections })

def create_collection(request):
    context = {}

    form = ItemCollectionForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    context['form'] = form
    
    return render(request, 'create_collection.html', { 'form': form })