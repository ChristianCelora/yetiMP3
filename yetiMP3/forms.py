from django import forms

class YTForm(forms.Form):
    url = forms.CharField()
    auto_id = False

    def __init__(self, *args, **kwargs):
        super(YTForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update({'id':'yt_url', 'class':'form-text'})

    #def send_email(self):
        # send email using the self.cleaned_data dictionary
        #pass