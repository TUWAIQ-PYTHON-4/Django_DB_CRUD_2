from django import forms
from .models import AboutModel


# creating a form
class AboutForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = AboutModel

        # specify fields to be used
        fields = [
            "name",
            "l_name",
        ]