from django.urls import path
# from .views import Teacherlist,
from . import views


urlpatterns = [
     # Teacher
     path('teacher/', views.TeacherList.as_view()),
     path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
     path('teacher/login/', views.TeacherLoginView.as_view(), name='teacher-login'),
     # Category
     path('category/', views.CategoryList.as_view()),
     # Course
     path('course/', views.CourseList.as_view()),

     #chapter
     path('chapter/', views.ChapterList.as_view()),
     # path('chapterdetails/', views.ChapterDetails.as_view()),
     path('chapterdetails/<int:pk>', views.ChapterDetails.as_view()),

     path ('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),
     # Teacher Courses
     path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),
     path('teacher-course-detail/<int:pk>', views.TeacherCourseDetail.as_view()),
     # Student
    #  path('student/', views.StudentList.as_view()),
 ]
