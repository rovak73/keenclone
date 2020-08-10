# from django import Modelform
from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['slug', 'user']

    # def __init__(self, *args, **kwargs):
    #     current_user = kwargs.pop('current_user')
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['user'] = current_user

   