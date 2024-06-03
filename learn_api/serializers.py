from rest_framework import serializers
# from .models import Course, Chapter, Student, Teacher
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name', 'email', 'password', 'qualification', 'mobile_no', 'skills']

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id','title','description']         

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id','category', 'teacher', 'title','description', 'featured_img', 'techs']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter 
        fields = ['id', 'course', 'title', 'description', 'video', 'remarks']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'full_name', 'username', 'email', 'password', 'interested_categories']  
