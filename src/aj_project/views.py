from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
# 장고 안에 데이터 뭉치안에 http안에 httpRespose 도구를 쓴다는 의미

def index(request):
    return HttpResponse("Hello, world. You're at the aj_project index.")
