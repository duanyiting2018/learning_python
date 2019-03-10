from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404
#from django.template import loader
def index(request):
      latest_question_list=Question.objects.order_by('-pub_date')[:5]
      #template=loader.get_template('polls/index.html')
      context={'latest_question_list':latest_question_list}
      output=', '.join([q.question_text for q in latest_question_list])
      return render(request,'polls/index.html',context)
def detail(request,question_id):
      """try:
            question=Question.objects.get(pk=question_id)
      except Question.DoesNotExist:
            raise Http404("没有这个题目。")"""
      question = get_object_or_404(Question, pk=question_id)
      return render(request,'polls/detail.html',{'question':question})
def results(request,question_id):
      response="这是第%s号题目的答案:"
      return HttpResponse(response%question_id)
def vote(request,question_id):
      return HttpResponse("空%s"%question_id)
