from rest_framework import serializers
from . import models

# Teacher Serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'