from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def info(request):
    return render(request, 'info.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        ask = request.POST.get('ask')
        contact = Contact(name=name, email=email, phone=phone,
                          ask=ask, date=datetime.today())
        contact.save()
        messages.success(
            request, 'Your message has been sent .We will get in touch with you soon')

    return render(request, 'contact.html')

def coaching(request):
    return render(request, 'coaching.html')

def team(request):
    return render(request, 'team.html')

def location(request):
    return render(request, 'location.html')
