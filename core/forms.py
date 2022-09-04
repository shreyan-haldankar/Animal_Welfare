from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'email-bt'})
            field.widget.attrs.update({'style': 'color:black;'})

            # field.widget.attrs.update({'placeholder': 'email-bt'})
            if name == "first_name":
                field.widget.attrs.update({'placeholder': 'Name'})
            elif name == "email":
                field.widget.attrs.update({'placeholder': 'Email'})
            elif name == "username":
                field.widget.attrs.update({'placeholder': 'Username'})
            elif name == "password1":
                field.widget.attrs.update({'placeholder': 'Enter your Password'})
            elif name == "password2":
                field.widget.attrs.update({'placeholder': 'Confirm your Password'})
            else:
                field.widget.attrs.update({'placeholder': 'Input'})




class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})