from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import  get_object_or_404,render
from django.template import loader
from .models import Choice,Question
# Create your views here.
from django.http import Http404
from .models import Question
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')# [:5]最近5个
    # output=', '.join([q.question_text for q in latest_question_list])
    # template=loader.get_template('polls/index.html')  #获取模板文件
    context={
        'latest_question_list':latest_question_list
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise  Http404("Question does not exist")
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{'question':question})

def result(request,question_id):
    response="You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        select_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice."
        })

    return HttpResponse("You're voting on question %s." %question_id)