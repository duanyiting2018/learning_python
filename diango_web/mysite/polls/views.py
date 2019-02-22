from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
      return HttpResponse("欢迎您，这里是duanyiting网页！如果你看到的话，你已成功了！恭喜你！")
