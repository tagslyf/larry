from django.views.generic import (CreateView,
                                  ListView,
                                  TemplateView,)
from django.urls import reverse_lazy

from .forms import UploadImageForm
from .models import UploadImage


class Index(TemplateView):
    template_name = 'index.html'


class UploadImageListView(ListView):
    model = UploadImage
    template_name = 'index.html'
    context_object_name = 'images'


class UploadImageView(CreateView):
    model = UploadImage
    form_class = UploadImageForm
    success_url = reverse_lazy('index')
