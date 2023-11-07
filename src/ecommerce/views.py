from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
  context = {
    "title": "Hello World!",
    "content": "Welcome to the home page."
  }
  return render(request, "home_page.html", context)

def about_page(request):
  context = {
    "title": "About Page",
    "content": "Welcome to the about page."
  }
  return render(request, "home_page.html", context)

def contact_page(request):
  context = {
    "title": "Contact",
    "content": "Welcome to the contact page."
  }
  if request.method == "POST":
    print(request.POST)
    print(request.POST.get("fullname"))
    print(request.POST.get("email"))
    print(request.POST.get("content"))
  return render(request, "contact/view.html", context)