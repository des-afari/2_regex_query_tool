from django import forms 

class RegexForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    regex = forms.CharField(label='Regular Expression')
    text_string = forms.CharField(widget=forms.Textarea())
    substitution = forms.CharField(widget=forms.Textarea())