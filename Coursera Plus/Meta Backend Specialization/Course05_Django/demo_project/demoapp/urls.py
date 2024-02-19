from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('gb/', views.say_goodbye, name='gb'),
    path('home/', views.homepage, name= 'home')
]