# Create your tasks here
from celery import shared_task
from yetiMP3.include.YTDownloader import YTDownloader

@shared_task
def download_yt_mp3(url, new_name):
    ytd = YTDownloader()
    real_name, client_name =  ytd.download(url, new_name)
    #update db
    return real_name, client_name
    
