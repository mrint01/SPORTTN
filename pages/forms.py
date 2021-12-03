from django.contrib.auth.models import User
from django import forms



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','password','email')
        widgets = {
              'first_name': forms.TextInput(
                attrs={
                    'placeholder': "Nom",
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
              'last_name': forms.TextInput(
                attrs={
                    'placeholder': "Prénom",
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': "Nom d'utilisateur",
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
             'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                    'style':'color:black',
                }
            ),
             'password': forms.PasswordInput(
                attrs={
                    'placeholder': "****************",
                    'style':'color:black',
                }
            ),
           
         }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': '**********************'})
      