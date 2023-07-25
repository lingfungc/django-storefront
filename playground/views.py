# Create your views here.

# * This "views" is essentially a request handler, which is not about HTML file
# * Take a Request -> Return a Response


from django.shortcuts import render
from django.http import HttpResponse

# * We can use these request handlers in django to:
# Pull data from database
# Transform data
# Send email

def say_hello(request):
    return HttpResponse("Hello World")
