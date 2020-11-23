from django import forms
from yetiMP3.include.YTDownloader import YTDownloader

class YTForm(forms.Form):
    #url = forms.URLField()
    url = forms.CharField()
    auto_id = False

    def __init__(self, *args, **kwargs):
        super(YTForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update({'id':'yt_url', 'class':'form-text'})
    """
        Downloads mp3 from youtube
    """
    def getMp3(self):
        print("url", self.cleaned_data['url'])
        url = self.cleaned_data['url']
        yt = YTDownloader()
        yt.download(url)
        pass