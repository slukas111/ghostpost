from django import forms
from posts.models import GhostPost

class AddForm(forms.ModelForm):
    class Meta:
        model = GhostPost
        # fields = '__all__'
        fields = ['post', 'is_boast']

