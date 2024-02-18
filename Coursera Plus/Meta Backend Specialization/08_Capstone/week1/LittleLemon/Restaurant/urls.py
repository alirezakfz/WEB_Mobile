from django.urls import path 
from .views import sayHello 
from . import views
  
urlpatterns = [ 
    path('hello', views.sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('message/', views.msg),
]