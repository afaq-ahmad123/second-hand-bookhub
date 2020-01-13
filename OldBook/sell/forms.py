from django import forms
from django.apps import apps

userInfo = apps.get_model('login','user')
book = apps.get_model('home','book')

class add_book(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' Book Title'}))
    price = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': ' Price (USD $)'}))
    writer = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' Writer Name'}))
    sellerID = forms.IntegerField()
    image = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = book
        fields = ['title','price','writer','sellerID', 'image']
    def authenticate_data(self):
        return True
