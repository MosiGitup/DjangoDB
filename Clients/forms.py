from django import forms
from .models import Profile
from django.contrib.auth.models import User


SelectDomain = [
    ('', 'Select the Project'),
    ('SPQ', 'SPQ Project'),
    ('BC', 'BC project'),
    ('Yukon', 'Yukon Project'),
    ]


class ProfileForm(forms.ModelForm):
    pass_conf = forms.CharField(max_length=50, label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation',
                                                                                           'name': 'client_pass_conf', 'id': 'client_pass_conf'}))

    class Meta:
        model = Profile
        fields = ('First_name', 'Last_name', 'Email', 'Username', 'Password', 'pass_conf', 'Domain')
        labels = {
            'First_name': '',
            'Last_name': '',
            'Email': '',
            'Username': '',
            'Password': '',
            'Domain': '',
        }
        widgets = {
            'First_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'Username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',
                                            'name': 'client_pass', 'id': 'client_pass'}),
            'Domain': forms.Select(choices=SelectDomain, attrs={'class': 'form-control', 'placeholder': 'Select the Project'}),
        }
