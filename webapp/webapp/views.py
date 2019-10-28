from django.core.files.storage import FileSystemStorage
from django.forms import modelformset_factory
from django.shortcuts import (render,
                              redirect)
from django.views.generic import (CreateView,
                                  ListView,
                                  TemplateView,)
from django.urls import reverse_lazy

from .forms import UploadImageForm
from .models import UploadImage


class Index(TemplateView):
    template_name = 'index.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES.get('document')
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def image_list(request):
    images = UploadImage.objects.all()
    return render(request, 'image_list.html', {'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = UploadImageForm()

    return render(request, 'upload_image.html', {'form': form})


class UploadImageListView(ListView):
    model = UploadImage
    template_name = 'class_image_list.html'
    context_object_name = 'images'


class UploadImageView(CreateView):
    model = UploadImage
    # form_class = UploadImageForm
    form_class = modelformset_factory(UploadImage,
                                      form=UploadImageForm,
                                      extra=3)
    success_url = 'class_image_list'
    template_name = 'class_upload_image.html'
