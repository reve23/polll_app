from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader
from django.urls import reverse

#get questions and display them
def index(request):
    #return a template
    #polls is our app name
    #index.html is our template file
    #folder structer is root ->templates->polls->index.html
    lates_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lates_question_list': lates_question_list}
    return render(request,'polls/index.html',context)

#show specific questions and choices
def detail(request,question_id):
    try:
        questions = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'questions':questions})

#get  questions and display results
def results(request,question_id):
    questions = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{"questions":questions})

#vote for a question choice
def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question': question,
            'error_message': 'you didnt selected a choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id)))