from .models import Files
from rest_framework import serializers
# remember to import the File model
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
class SaveFileSerializer(serializers.Serializer):
    class Meta:
        model = Files
        fields = "__all__"