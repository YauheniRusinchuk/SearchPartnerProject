from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label="Your Email",)
    password = forms.CharField(label="Your Password",widget=forms.PasswordInput(
            attrs={'placeholder': 'password ...'}
    ))

    email.widget.attrs.update({'placeholder': 'email ...'})
