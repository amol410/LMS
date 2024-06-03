from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Teacher, CourseCategory, Course, Chapter
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CourseCategorySerializer, CourseSerializer, TeacherSerializer, ChapterSerializer


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class TeacherLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            teacher = Teacher.objects.get(email=email, password=password)
            serializer = TeacherSerializer(teacher)
            return Response({'bool': True, 'teacher': serializer.data})
        except Teacher.DoesNotExist:
            return Response({'bool': False, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class CategoryList(generics.ListCreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     limit = (self.request.GET('result', 10))
    #     qs = Course.objects.all().order_by('-id')[:limit]

    #     if 'category' in self.request.GET:
    #         category = self.request.GET['category']
    #         qs = Course.objects.filter(techs_icontains=category)

    #     if 'skill_name' in self.request.GET and 'teacher' in self.request.GET:
    #         skill_name = self.request.GET['skill_name']
    #         skill_name = self.request.GET['teacher']
    #         teacher = Teacher.objects.filter(id=skill_name).first()
    #         qs= Course.objects.filter(techs_icontains=skill_name, teacher=teacher) 

    #     return qs       




class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer    


class ChapterList(generics.ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class ChapterDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer   

    

class TeacherCourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = Teacher.objects.get(pk=teacher_id)
        return Course.objects.filter(teacher=teacher)
    
    """above code Course.objects.filter(teacher=teacher)  
    retrieves all the Course objects from the database whose teacher field 
    matches the teacher instance 
    obtained in the previous line."""

class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

class CourseChapterList(generics.ListAPIView):
    serializer_class = ChapterSerializer
    
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = Course.objects.get(pk=course_id)
        return Chapter.objects.filter(course=course)     