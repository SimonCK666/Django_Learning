from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

def index(request):
    html = render_to_string("")