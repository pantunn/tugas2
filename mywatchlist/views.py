from django.shortcuts import render
from mywatchlist.models import Item_MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_mywatchlist = Item_MyWatchList.objects.all()
    context = {
        'list_movie': data_mywatchlist,
        'nama': 'Pantun Elfreddy',
        'NPM' : '2106751612',
        
        }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    data_mywatchlist = Item_MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_mywatchlist_json(request):
    data_mywatchlist = Item_MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def kembalikan_data_xml(request, id):
    data_mywatchlist = Item_MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml") 

def kembalikan_data_json(request, id):
    data_mywatchlist = Item_MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

