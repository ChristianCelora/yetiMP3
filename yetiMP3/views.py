import os
from django.shortcuts import render
from . import forms
from django.forms.models import model_to_dict 
from django.views.generic.edit import FormView
from django.http import HttpResponse, JsonResponse
from yetiMP3.include.YTDownloader import YTDownloader
from yetiMP3.tasks import download_yt_mp3

from yetiMP3.models import Task

# Create your views here.
# AJAX Handlers
def download_from_yt(request):
    url = request.POST.get("url", None)
    new_name = request.POST.get("name", "")
    ytd = YTDownloader()
    real_name, client_name = ytd.download(url, new_name)
    data = {"status": False, "name": "", "id": ""}
    if os.path.exists(os.path.join(ytd.download_dir, real_name+".mp3")):
        data = {"status": True, "name": client_name, "id": real_name}
    return JsonResponse(data)

def download_from_yt_async(request):
    url = request.POST.get("url", None)
    new_name = request.POST.get("name", "")
    try:
    # make unique id 
        task_unique_id = 1
        # add task to queue
        task = Task(status = 0)
        task.save()
        download_yt_mp3.delay(url, new_name, task.id)
        data = {"status": True, "task_id": task.id}
    except Exception as e:
        data = {"status": False, "task_id": ""}

    return JsonResponse(data)

def check_task(request):
    task_id = request.POST.get("task_id", None)
    if task_id != None:
        task = Task.objects.get(id=task_id)
        data = {"status": True, "task": model_to_dict(task)}
    else:
        data = {"status": False}

    return JsonResponse(data)


def download_mp3(request, id, name):
    client_name = name + ".mp3"
    file_path = os.path.join(YTDownloader().download_dir, id+".mp3")
    print("download mp3", file_path)
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

    