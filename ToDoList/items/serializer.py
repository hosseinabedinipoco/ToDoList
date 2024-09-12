from pathlib import __all__
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['published_date', 'author']

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        validated_data['author'] = author
        return super().create(validated_data)    