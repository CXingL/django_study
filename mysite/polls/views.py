# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django import forms
from polls import models
from .models import Question, Choice, User

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def ExampleView(request):
    error_msg = ""
    if request.method == 'POST':

        uf = UserForm(request.POST)

        if 'login' in request.POST:
            if uf.is_valid():
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']

                user = User.objects.filter(username__exact=username,password__exact=password)
                if user:
                    return render(request, 'polls/login.html')
                else:
                    error_msg = "email or password error, please try again"
        else:
            if uf.is_valid():
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                User.objects.create(username = username, password = password)
                return render(request, 'polls/login.html',{'uf':uf})
            else:
                error_msg = "Please enter your email"
    else:
        uf = UserForm()
    return render(request, 'polls/example.html', {"error_msg": error_msg})
    
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username = username, password = password)
            return render(request, 'polls/login.html',{'uf':uf})
        else:
            return render(request, 'polls/example.html')
    
    else:
        uf = UserForm()
    
    return render(request, 'polls/regist.html',{'uf':uf})


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}

#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

