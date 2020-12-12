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
    ytd = YTDownloader()
    real_name, client_name = ytd.download(url)
    data = {"status": False, "name": "", "id": ""}
    if os.path.exists(os.path.join(ytd.download_dir, real_name+".mp3")):
        data = {"status": True, "name": client_name, "id": real_name}
    return JsonResponse(data)

def download_mp3():
    real_name = request.GET.get("id", None)
    client_name = request.GET.get("name", None)
    file_path = os.path.join(YTDownloader().download_dir, real_name+".mp3")
    print("download", file_path)
    with open(file_path, "rb") as fh:
        response = HttpResponse(fh.read(), content_type="audio/mpeg")
        response['Content-Disposition'] = 'attachment; filename="'+os.path.basename(client_name)+'"'
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

    