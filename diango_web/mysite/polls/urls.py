from django.urls import path
from .import views
urlpatterns=[path('dyt',views.index,name='index')]
