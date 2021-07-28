from django.shortcuts import render


def index(request):
    return render(request, "socketapp/index.html", context={'text': "Let's Start!"})
