from django.shortcuts import render
# from django.http import HttpResponse
from .models import Article
# Create your views here.
# 장고 안에 데이터 뭉치안에 http안에 httpRespose 도구를 쓴다는 의미


def index(request):
    # name = "ajkim"
    # return render(request, "index.html", {"name": name})
    article_list = Article.objects.all()
    # Article.objects.create(
    #     title="hello",
    #     contents="this is test",
    #     view_count=0
    # )
    ctx = {
        "article_list" : article_list
    }
    return render(request, "index.html", ctx)
