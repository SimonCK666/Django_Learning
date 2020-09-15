from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template.loader import render_to_string

def index(request):
    return render_to_string(request, "front/index.html")
    # return HttpResponse(html)