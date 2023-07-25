# Create your views here.

# * This 'views' is essentially a request handler, which is not about HTML file
# * Take a Request -> Return a Response


from django.shortcuts import render
from django.http import HttpResponse

# * We can use these request handlers in django to:
# Pull data from database
# Transform data
# Send email

# * We need to map this view (request handler) to a url in 'urls.py'

def say_hello(request):
    # return HttpResponse('Hello World')

    # 1st argument: The "request" itself
    # 2nd argument: The HTML file name
    # 3rd argument: The mapping object (which is dictionary in Python)
    return render(request, 'hello.html', {'name': 'lingfungc'})
