from django.shortcuts import render

def bugsView(request):

    return render(request, "bug-tracker/bugs-view.html")
