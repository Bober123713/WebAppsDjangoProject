from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'required': 'required',
                                                                           'type': 'email',
                                                                           'placeholder': 'exmaple@email.com',
                                                                           'maxlength': '254', }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'required': 'required',
                                               'type': 'text',
                                               'placeholder': 'username',
                                               'maxlength': '150', }),
            'password1': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'required': 'required',
                                                    'type': 'password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'required': 'required',
                                                    'type': 'password'}),
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()
        return user
