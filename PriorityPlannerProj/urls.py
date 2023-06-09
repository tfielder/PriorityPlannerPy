"""PriorityPlannerProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from itemCollectionApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("collections", views.collections, name="collections"),
    path("create-collection", views.create_collection, name="create-collection"),
    path("collections/<int:collection_id>/", views.collection_detail, name="collection_detail"),
    path("collections/<int:collection_id>/create-item/", views.create_item, name="create-item"),
    path("collections/<int:collection_id>/items/<int:item_id>/", views.item_detail, name="item_detail"),
    path("collections/<int:collection_id>/collection-sorter/", views.collection_sorter, name="collection_sorter"),
    path("collections/<int:collection_id>/delete", views.delete_collection, name="collection_delete")
]
