from django.shortcuts import render

def showindex(request):
    return render(request, "index.html")


def registeruser(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "suchishree" and password=="badjena":
        return render(request, "welcome.html")
    else:
        return render(request, "error.html")