import os
from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.views.generic.edit import FormView
from yetiMP3.include.YTDownloader import YTDownloader
from django.http import JsonResponse

# Create your views here.
# AJAX Handlers
def download_from_yt(request):
    url = request.POST.get('url', None)
    real_name, client_name = YTDownloader().download(url)
    data = {"status": False, "file": "", "id": ""}
    if os.path.exists(real_name):
        data = {"status": False, "file": client_name, "id": real_name}
    return JsonResponse(data)

def download():
    filename = request.GET.get("filename", None)
    file_path = os.path.join(YTDownloader().download_dir, filename)
    print("download", file_path)
    with open(file_path, "rb") as fh:
        response = HttpResponse(fh.read(), content_type="audio/mpeg")
        response['Content-Disposition'] = 'attachment; filename="'+os.path.basename(file_path)+'"'
        return response

# Classic form handler
class IndexView(FormView):
    template_name = 'yt_form.html'
    form_class = forms.YTForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # url -> mp3
        file_path = form.downloadMp3()
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="audio/mpeg")
                response['Content-Disposition'] = 'attachment; filename="'+os.path.basename(file_path)+'"'
                return response
        return super().form_valid(form)

    