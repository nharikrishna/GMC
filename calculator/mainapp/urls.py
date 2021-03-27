from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='home'),
    path('check', views.check_view, name='check'),
    path('logout', views.logout_view, name='logout'),
    path('advisor/view_profile', views.view_profile_advisor_view, name='view_profile_advisor'),
    path('advisor/class_details', views.class_details_view, name='class_details'),
    path('student/view_profile', views.view_profile_student_view, name='view_profile_student'),
    path('student/view_marks', views.view_marks_view, name='view_marks'),
    path('faculty/view_profile', views.view_profile_faculty_view, name='view_profile_faculty'),
    path('faculty/view_course', views.view_course_faculty_view, name='view_course_faculty'),
    path('faculty/view_marks/<str:course_title>', views.view_marks_faculty_view, name='view_marks_faculty'),
    path('faculty/update_marks', views.update_marks_view, name='view_update_marks'),
    path('coe/view_profile', views.view_profile_coe_view, name='view_profile_coe'),
]