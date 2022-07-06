from django.http import HttpResponse

def home(request):
    text = """My project"""

    return HttpResponse(text)