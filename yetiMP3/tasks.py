# Create your tasks here
from celery import shared_task
from celery.utils.log import get_task_logger
from yetiMP3.include.YTDownloader import YTDownloader

from yetiMP3.models import Task

logger = get_task_logger(__name__)

@shared_task
def download_yt_mp3(url, new_name, task_id):
    ytd = YTDownloader()
    logger.info("Starting download, url: "+url)
    real_name, client_name =  ytd.download(url, new_name)
    #update db
    task = Task.objects.get(id=task_id)
    if(task):
        task.status = 1
        task.file_name = real_name
        task.frontend_name = client_name
        task.save()