from django.urls import path
from .import views
urlpatterns=[#/polls/
      path('',views.index,name='index'),
      #/polls/question_id/
      path('<int:question_id>/',views.detail,name='detail'),
      #/polls/question_id/results/
      path('<int:question_id>/results/',views.results,name='results'),
      #/polls/question_id/vote/
      path('<int:question_id>/vote/',views.vote,name='vote')]
