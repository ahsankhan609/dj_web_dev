from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request) -> HttpResponse:
    """
    This function is a view that handles the HTTP GET request to the home page.
    It returns an HTTP response to the client.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response to send back to the client.
    """
    # Create an empty HTTP response
    # We will add the response here that we need to show to the client.
    # It could be an HTML file, a JSON response, or any other type of response
    # that the client expects.
    return HttpResponse("Read Quran every day in January!")


def february(request) -> HttpResponse:
    return HttpResponse("Walk for atleast 5km in february!")


def march(request) -> HttpResponse:
    return HttpResponse("Read Hadees every day in march!")
