from rest_framework import serializers
from .models import File, UserProfile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'uploaded_at', 'category', 'tags']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['preferred_sorting_method']
