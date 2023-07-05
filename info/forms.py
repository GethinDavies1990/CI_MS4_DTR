from django import forms
from .models import Teams


class TeamsForm(forms.ModelForm):

    class Meta:
        model = Teams
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)