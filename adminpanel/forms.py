from django import forms

from database.models import website

class WebSiteForm(forms.ModelForm):
    class Meta:
        model = website
        fields = ("name","description", "note", "url", "author", "security")
