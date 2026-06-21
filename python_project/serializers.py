from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

    def to_internal_value(self, data):
        if 'type' in data and isinstance(data['type'], list):
            data['type'] = ", ".join(data['type'])
        return super().to_internal_value(data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'email', 'password']    
