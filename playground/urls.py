from django.urls import path
from . import views


# * URLconf
# * We need to include this new URLconf in 'storefront/urls.py'
urlpatterns = [
    # 1st argument: Route in a 'String'
    # 2nd argument: View as a Reference only (We're not calling the function)
    # * We always end our route with the forward slash '/'
    path('hello/', views.say_hello)
]
