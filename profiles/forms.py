# from django import Modelform
from django.core.files import File
from .models import Profile
from django import forms
from PIL import Image




class ProfileFormPub(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'picture',
            'profile_name',
            'profile_excerpt',
            'profile',
            'specialty',
            ]
        widgets = {'specialty':  forms.CheckboxSelectMultiple()} 
    # def __init__(self, *args, **kwargs):
    #     current_user = kwargs.pop('current_user')
    #     super(ProfileFormPub, self).__init__(*args, **kwargs)
    #     self.fields['user'] = current_user

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super(ProfileFormPub, self).__init__(*args, **kwargs)
    #     user = Profile.objects.get(user=user)
    

    # def __init__(self, *args, **kwargs):
    #    self.request = kwargs.pop('request', None)
    #    return super(ProfileFormPub, self).__init__(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #    kwargs['commit']=False
    #    obj = super(ProfileFormPub, self).save(*args, **kwargs)
    #    if self.request:
    #        obj.user = self.request.user
    #    obj.save()
    #    return obj


class ProfileFormPrv(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'address',
            'city',
            'country',
            'rut',
            ]

class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Profile
        fields = ('picture', 'x', 'y', 'width', 'height', )

    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(profile.picture)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(profile.picture.path)

        return photo