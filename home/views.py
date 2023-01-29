from django.shortcuts import render


def index(request):
    """
    Home page view
    """
    return render(request, "home/index.html")


def AboutUs(request):
    """
    About us page view
    """
    return render(request, "home/about_us.html")
