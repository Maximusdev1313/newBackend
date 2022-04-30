from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'massage', 'date']