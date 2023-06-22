from django.shortcuts import render

from . import util
import os
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    print("i am title.")
    list_entries=util.list_entries()
    print(list_entries)
    if title not in list_entries:
        return render(request,"encyclopedia/error0.html")
    else:
        return render(request,"encyclopedia/title.html",{
            "title":title,
            "returntitle":util.get_entry(title)
        })

def search(request):
    print("i am search.")
    list_entries=util.list_entries()
    if request.method=="POST":    
        title=request.POST["q"]   
        if title in list_entries:
            return render(request,"encyclopedia/title.html",{
                "title":title,
                "returntitle":util.get_entry(title)
            })
        else:
            possible=[]
            for j in range(len(list_entries)):
                if title in list_entries[j]:
                    possible.append(list_entries[j])
            return render(request, "encyclopedia/posindex.html", {"entries": possible})

def create(request):
    list_entries=util.list_entries()
    if request.method=="POST":
        newtitle=request.POST["newtitle"]
        newtitle=newtitle.replace(" ", "")
        print(newtitle)
        newdef=request.POST["newdef"]
        if newtitle not in list_entries:
            newfile=open("./entries/"+newtitle+".md","w")
            newfile.write(newdef)
            newfile.close()
            return render(request,"encyclopedia/title.html",{
            "title":newtitle,
            "returntitle":util.get_entry(newtitle)
            })
        else:
            return render(request,"encyclopedia/error1.html")

    else:
        return render(request, "encyclopedia/create.html")
    
                
def edit(request):
    if request.method=="POST":
        edittitle=request.POST["edittitle"]
        return render(request,"encyclopedia/edit.html",{
            "title":edittitle,
            "curcontent":util.get_entry(edittitle)
        })
          
def editedpage(request):
    editdef=request.POST["editdef"]
    newtitle=request.POST["edittitle"]
    newtitle=newtitle.replace(" ", "")    
    newfile=open("./entries/"+newtitle+".md","w")
    newfile.write(editdef)
    newfile.close()
    return render(request,"encyclopedia/title.html",{
        "title":newtitle,
        "returntitle":util.get_entry(newtitle)
    })

def rand(request):
    enlist=util.list_entries()
    title=random.choice(enlist)

    return render(request,"encyclopedia/title.html",{
            "title":title,
            "returntitle":util.get_entry(title)
        })



        
