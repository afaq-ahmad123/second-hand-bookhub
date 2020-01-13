from django import forms
from django.apps import apps


userInfo = apps.get_model('login','user')


class profileEditForm(forms.ModelForm):
    class Meta:
        model = userInfo
        fields = ['name', 'contact','password','address']

