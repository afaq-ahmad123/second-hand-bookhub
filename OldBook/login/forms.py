from django import forms
from django.apps import apps
userInfo = apps.get_model('login' , 'user')

class LoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': ' Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': ' Password'}))

    class Meta:
        model = userInfo
        fields = ['email', 'password']

    def authenticate_data(self, email, password):
        user = userInfo.objects.filter(email=email)
        if not user:
            return True
        user = userInfo.objects.get(email=email)
        if user.password != password:
            return False
        return True

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'col-md-10 '


class UserForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' Name'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': ' Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': ' Password'}))
    confirm = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': ' Confirm Password'}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' Address'}))
    contact = forms.RegexField(regex=r'^\+?1?\d{9,15}$', widget=forms.TextInput(
        attrs={'placeholder': ' Conatact no. (+99999999)'}))


    class Meta:
        model = userInfo
        fields = ['name', 'email', 'password', 'address', 'contact']

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     confirm = self.cleaned_data.get('confirm')
    #     if len(password) < 6:
    #         raise forms.ValidationError("Password should be 6 or more characters long")
    #     elif password != confirm:
    #         raise forms.ValidationError("Password not same")
    #     return password
    def authenticate_data(self, email, password):
        user = userInfo.objects.filter(email=email)
        if user:
            raise forms.ValidationError("User Already Exists.")
            return False
        return True
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'col-md-12 col-sm-12  col-lg-12 '

