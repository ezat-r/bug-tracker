from django.shortcuts import render
from bugDB.models import Issue
from django.contrib.postgres.search import SearchVector


def search(request):
    
    # perform a vector search using the issue 'title' & 'description' properties
    issues = Issue.objects.annotate(
        search=SearchVector('title', 'description'),
        ).filter(search=request.GET["query"])
    
    # return results to view
    return render(request, "search/search-results.html", {"issues": issues, "query": request.GET["query"]})
