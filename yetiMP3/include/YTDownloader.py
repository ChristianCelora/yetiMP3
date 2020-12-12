import sys
import os
import youtube_dl.utils
import eyed3
from youtube_dl import YoutubeDL
from django.conf import settings

class YTDownloader:
    def __init__(self):
        self.download_dir = settings.STORAGE_DIR

    def download(self, uri: str, new_name="") -> str:
        outputname = ""
        ydl_opts = self.__getOptions()
        with YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(uri, download=True)
                real_name = info["id"]
                outputname = ydl.prepare_filename(info).replace(".mp4", ".mp3")
                ydl.download([uri])
                self.renameFile(outputname, real_name)
                if new_name != "":
                    self.changeMp3Metadata(outputname, new_name)
            except youtube_dl.utils.SameFileError as sfe:
                print("File già esistente: "+str(sfe))
            except youtube_dl.utils.DownloadError as de:
                print(str(de))
        # return os.path.join(self.download_dir, outputname)
        return real_name, outputname

    def __getOptions(self) -> dict:
        opt = {
                "outtmpl": os.path.join(self.download_dir, "%(title)s.mp4"),   
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192"
                }],
            } # scarica la canzione in .mp4 e la converte in .mp3 con FFmpeg

        return opt

    def renameFile(self, old_path: str, name: str) -> str:
        filepath = self.getUniqueName(name)
        os.rename(old_path, filepath)
        return name

    def changeMp3Metadata(self, path: str, name: str):
        audiofile = eyed3.core.load(path)
        if not audiofile is None:
            title, artist = name.split("-", 1)
            audiofile.tag.artist = artist.strip()
            audiofile.tag.title = title.strip()
            audiofile.tag.save()

    def getUniqueName(self, filename: str) -> str:
        filepath = os.path.join("Download", filename+".mp3")
        # check if file alredy exist
        if os.path.exists(filepath):
            i = 1
            while os.path.exists(filepath):
                filepath = os.path.join("Download", filename+"_"+str(i)+".mp3")
                i += 1
        return filepath