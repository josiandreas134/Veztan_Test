from django.test import SimpleTestCase
from visiondemo.forms import URLForm, UploadFileForm
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import tempfile

class TestForms(SimpleTestCase):
    def test_URLForm_with_valid_data(self):
        url = {'myinput' : "http://places.csail.mit.edu/demo/3.jpg"}
        form = URLForm(url)
        self.assertTrue(form.is_valid())

    def test_URLForm_with_no_data(self):
        form = URLForm()
        self.assertFalse(form.is_valid())

    def test_UploadFileForm_with_valid_data(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        img = {'file':tmp_file}
        form = UploadFileForm(img)
        self.assertFalse(form.is_valid())

    def test_UploadFileForm_with_no_data(self):
        form = UploadFileForm()
        self.assertFalse(form.is_valid())
