from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()



class RegisterForm(forms.ModelForm):

    password    = forms.CharField(widget=forms.PasswordInput)
    firstname   = forms.CharField(max_length=100)
    lastname    = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    img         = forms.ImageField(label='Your image')

    class Meta:
        model = User
        fields = ['email']
