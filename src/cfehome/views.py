import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    # qs = PageVisit.objects.all()
    # page_qs = PageVisit.objects.filter(path=request.path)
    # context = {
    #     "page_title": "My Page",
    #     "page_visit_count": page_qs.count(),
    #     "total_visit_count": qs.count()

    # }
    # path = request.path
    
    html_template = "home.html"
    context={}
    # PageVisit.objects.create(path=request.path)
    return render(request, html_template, context)