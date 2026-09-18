from django.shortcuts import render

def about_view(request, name):
    return render (
        request,
        "home/about.html",
        {
            "name" : name
        }
    )