from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from.models import Question
from django.template import loader
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    #output = ", ".join([q.question_text for q in latest_question_list]) this is for a completely static view
    context = { 
        "latest_question_list": latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context) #if i don't add dictionary, the polls break


def detail(request, question_id):
    # try: the longer way without django.shortcuts
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# With this function, it would overwrite the above detail function
# def detail(request, question_id):
#     return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

#/vote/42/some-text/
#vote(request, question_id=42, extra_string="some-text")

