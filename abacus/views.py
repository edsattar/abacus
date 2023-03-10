from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

# Create your views here.
class TeacherList(APIView):
    def get(self, request):
        teachers = models.Teacher.objects.all()
        serializer = serializers.TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
