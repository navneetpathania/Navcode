from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home-page'),
    path('about/',views.about,name='about-page'),
    path('skills/',views.skills,name='skills-page'),
    path('work/',views.work,name='work-page'),
    path('education/',views.education,name='education-page'),
    path('contact/',views.contact,name='contact-page'),
    
   
]