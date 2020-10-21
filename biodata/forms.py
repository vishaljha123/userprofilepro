from django import forms
from .models import Userinfo




class userregisterform(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = "__all__"


class userupdateform(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ('name','username','password','photo')



