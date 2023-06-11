from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")
    
# Create your views here.
def index(request):

    # We need to create session so that different users have different pages. (Like you open this page in different chromes you can see different tasks.)
    if "tasks" not in request.session:
        # We store tasks in this list or table as requested by django
        request.session["tasks"]=[]

    return render(request,"tasks/index.html",{
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method=="POST":
        # We store user input in the variable form
        form=NewTaskForm(request.POST)
        if form.is_valid():
            # Clean the input and store it in task
            task=form.cleaned_data["task"]
            # Add it to the task table/list
            request.session["tasks"]+=[task]
            # Here we user reverse because we usually do not hardcode a link, prefer to user its name
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                # We feed the html what the user just input so that the user can get why it is unqualified/invalid
                "form":form
            })
    return render(request,"tasks/add.html",{
        "form": NewTaskForm()
    })