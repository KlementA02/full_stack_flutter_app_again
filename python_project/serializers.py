from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

    def to_internal_value(self, data):
        mutable_data = data.copy() if hasattr(data, 'copy') else dict(data)
        if 'type' in mutable_data and isinstance(mutable_data['type'], list):
            mutable_data['type'] = ", ".join(mutable_data['type'])
        return super().to_internal_value(mutable_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if representation.get('type'):
            representation['type'] = [t.strip() for t in representation['type'].split(',')]
            
        return representation
    
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'email', 'password']    
