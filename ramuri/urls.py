from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='course_list'),
    # Specifiying a class based view (as_view() returns a function from the view)
    # path(route='course', view = views.CourseView.as_view(), name='course')
]