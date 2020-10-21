from rest_framework import serializers
from .models import Userinfo

class UesrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = ['name','username','email_add','photo']
        write_only_fields = ('name','username','photo','password')
