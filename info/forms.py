# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms

# Internal:
from .models import Teams

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TeamsForm(forms.ModelForm):
    """
    Class for the TeamsForm
    """

    class Meta:
        """
        A class for the Meta of Teams
        """

        model = Teams
        fields = "__all__"

    image = forms.ImageField(label="Image", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.label = True
            field.widget.attrs["class"] = "border-black rounded-0"
