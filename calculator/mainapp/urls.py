from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='home'),
    path('check', views.check_view, name='check'),
    path('logout', views.logout_view, name='logout'),
    path('advisor/view_profile', views.view_profile_advisor_view, name='view_profile_advisor'),
    path('advisor/class_details', views.class_details_view, name='class_details'),
    path('advisor/view_course', views.view_course_advisor_view, name='view_course_advisor'),
    path('advisor/view_grade/<str:course_title>', views.view_grade_advisor_view, name='view_grade_advisor'),
    path('advisor/view_marks', views.view_marks_advisor_view, name='view_marks_advisor'),
    path('student/view_profile', views.view_profile_student_view, name='view_profile_student'),
    path('student/view_marks', views.view_marks_view, name='view_marks'),
    path('faculty/view_profile', views.view_profile_faculty_view, name='view_profile_faculty'),
    path('faculty/view_course', views.view_course_faculty_view, name='view_course_faculty'),
    path('faculty/view_course_update', views.view_course_update_faculty_view, name='view_course_update_faculty'),
    path('faculty/view_marks/<str:course_title>', views.view_marks_faculty_view, name='view_marks_faculty'),
    path('faculty/update_marks/<str:course_title>', views.update_marks_view, name='update_marks'),
    path('faculty/view_course_grade', views.view_course_grade_view, name='view_course_grade'),
    path('faculty/view_grade/<str:course_title>', views.view_grade_faculty_view, name='view_grade_faculty'),
    path('coe/view_profile', views.view_profile_coe_view, name='view_profile_coe'),
    path('coe/view_course', views.view_course_coe_view, name='view_course_coe'),
    path('coe/update_grade/<str:course_title>', views.update_grade_view, name='update_grade')
]