from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang_katalog' : data_barang_katalog,
        'nama': 'Pantun Elfreddy',
        'NPM' : '2106751612',
        }
    return render(request, "katalog.html", context)
