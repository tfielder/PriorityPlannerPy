from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import CollectionItem, ItemCollection
from .forms import CollectionItemForm, ItemCollectionForm

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
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('collections'))

    context['form'] = form
    
    return render(request, 'create_collection.html', { 'form': form })

def create_item(request, collection_id):
    context = {}

    form = CollectionItemForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('collections'))

    context['form'] = form

    return render(request, 'create_item.html', { 'form': form, 'collection_id': collection_id })


def collection_detail(request, collection_id):
    try:
        collection = ItemCollection.objects.get(id=collection_id)
    except:
        raise Http404('Collection not found')
    
    return render(request, 'collection_detail.html', { 'collection': collection})


def item_detail(request, item_id):
    try:
        item = CollectionItem.objects.get(id=item_id)
    except:
        raise Http404('Item not found')

    return render(request, 'item_detail.html', { 'item': item })