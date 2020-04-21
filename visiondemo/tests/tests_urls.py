from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from visiondemo.views import index, fileupload, result


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('visiondemo:index')
        self.assertEquals(resolve(url).func , index)

    def test_fileupload_url_is_resolved(self):
        url = reverse('visiondemo:fileupload')
        self.assertEquals(resolve(url).func , fileupload)

    def test_result_url_is_resolved(self):
        url = reverse('visiondemo:result')
        print(resolve(url))
        self.assertEquals(resolve(url).func , result)
