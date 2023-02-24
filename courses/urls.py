# Imports
# 3rd party:
from django.urls import path, include
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path(
        '',
        views.Courses.as_view(),
        name='courses',
        ),
    path(
        'add_course/',
        views.AddCourse.as_view(),
        name='add_course',
        ),
    path(
        '<id_post>/',
        views.CourseDetails.as_view(),
        name='course_datails',
        ),
]
