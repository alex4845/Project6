from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from shtors.models import List1, List2, User_list, User_question


def main_page(request):
    list1s = List1.objects.all()
    return render(request, "shtors/index.html", {"list1s": list1s})

def in_list1(request, pk):
    category = List1.objects.get(pk=pk)
    list2s = category.list2_set.all()
    return render(request, "shtors/in_list1.html", {"category": category, "list2s": list2s})

def in_list2(request, pk):
    category = List2.objects.get(pk=pk)
    list3s = category.list3_set.all()
    return render(request, "shtors/in_list2.html", {"category": category, "list3s": list3s})

def registration(request):

    if request.method == "GET":
        return render(request, "shtors/registration.html")
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        post = request.POST["post"]
        try:
            us = User.objects.get(username=username)
            return render(request, "shtors/registration.html", {"us": us})
        except:
            user = User.objects.create_user(username=username, password=password, email=post)
            login(request, user)
            return redirect("Главная")

def enter_user(request):

    if request.method == "GET":
        return render(request, "shtors/enter.html")
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Главная")
        else:
            return render(request, "shtors/enter.html", {"username": username})


def exit_user(request):
    logout(request)
    return redirect("Вход")

def calendar(request):

    if request.method == "GET":
        return render(request, "shtors/calendar.html")
    if request.method == "POST":
        date = request.POST["date"]
        name = request.user.username
        try:
            b = User_list.objects.get(date_go=date)
            return render(request, "shtors/calendar.html", {"b": b, "name": name})
        except:
            a = User_list(name=name, date_go=date)
            a.save()
            return render(request, "shtors/calendar.html", {"date": date, "name": name})

def question(request):

    if request.method == "GET":
        return render(request, "shtors/question.html")
    if request.method == "POST":

        if request.user.is_authenticated:
            ques = request.POST["question"]
            name = request.user.username
            a = User_question(name=name, question=ques)
            a.save()
            return render(request, "shtors/question.html", {"ques": ques})
        else:
            b = "хрен"
            return render(request, "shtors/question.html", {"b": b})