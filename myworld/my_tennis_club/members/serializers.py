from rest_framework import serializers
from .models import *

class CorpRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = CorpRegister
		fields = "__all__"