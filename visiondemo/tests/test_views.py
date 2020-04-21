from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from PIL import Image
from django.http import HttpResponse, HttpResponseRedirect, Http404
import uuid
import tempfile
import json
import os

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('visiondemo:index')
        self.result_url = reverse('visiondemo:result')
        self.fileupload_url = reverse('visiondemo:fileupload')
        

    def test_index_GET(self):

        response = self.client.get(self.index_url)
        
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response,'visiondemo/demo.html')

    def test_fileupload_POST(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        response = self.client.post(self.fileupload_url, {'file': tmp_file}, format='multipart')

        self.assertEquals(response.status_code,302)

        response2 =self.client.get(self.result_url,follow=True)
        self.assertEquals(response2.status_code,200)


    def test_result_GET(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        response = self.client.post(self.fileupload_url, {'file': tmp_file}, format='multipart')

        response2 =self.client.get(self.result_url,follow=True)
        self.assertEquals(response2.status_code,200)


    #def test_fileupload_url_POST(self):
    #    response = self.client.post(self.fileupload_url, {'myinput': "http://places.csail.mit.edu/demo/3.jpg"},format='multipart' )
    #    self.assertEquals(response.status_code,302)
        #It stucks here, I try to do it in the website and it also stucks there.
        #Stucks in download succeeded.

