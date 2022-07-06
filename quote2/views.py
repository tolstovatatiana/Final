from django.shortcuts import render
from .models import Quote
# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string

def home_view(request):
    quote_objs = Quote.objects.all()

    context = {
        "quote_objects": quote_objs
    }
    # Template (html file)
    HTML_STRING = render_to_string("news.html", context)
    return HttpResponse(HTML_STRING)