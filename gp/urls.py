from django.urls import path
from . import views

urlpatterns = [
    # Add more URL patterns here
    path('api/data/', views.data, name='data'),
    path("", views.main, name="main"),
    path("api/ownerData/", views.ownerData, name="ownerData"),
    path("api/mentorData/", views.mentorData, name="mentorData"),
    path("student/<int:phone>", views.student, name="student"),
    path("api/finalMentor/", views.finalMentor, name="finalMentor"),

]
