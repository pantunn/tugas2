#from http import client 
#from multiprocessing.connection import Client 
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from mywatchlist.views import show_mywatchlist,show_mywatchlist_json,show_mywatchlist_xml



class Test(SimpleTestCase):


    def test_url_show_mywatchlist(self):
        response = reverse('mywatchlist:show_mywatchlist')
        self.assertEqual(resolve(response).func, show_mywatchlist)


    def test_url_show_mywatchlist_json(self):
        response = reverse('mywatchlist:show_mywatchlist_json')
        self.assertEqual(resolve(response).func, show_mywatchlist_json)


    def test_url_show_mywatchlist_xml(self):
        response = reverse('mywatchlist:show_mywatchlist_xml')
        self.assertEqual(resolve(response).func, show_mywatchlist_xml)
