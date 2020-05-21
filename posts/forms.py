from django import forms
from posts.models import Ghostpost

class AddForm(forms.Form):
    textinput = forms.CharField(widget=forms.Textarea)
    is_boast = forms.BooleanField(widget=forms.CheckboxInput, required=False)  