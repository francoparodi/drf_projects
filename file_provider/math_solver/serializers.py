from rest_framework import serializers
from .models import Solution, UploadedFile

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'status', 'output')


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'content', 'uploaded_at']