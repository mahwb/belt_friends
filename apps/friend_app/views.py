# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Users, Friends

# show index page
def index(request):
    # Friends.objects.all().delete()
    if not request.session["logged_in"]:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    data = {
        "friends": Friends.objects.all().order_by("-created_at")[:3]
    }
    return render(request, "friend_app/index.html", data)

# show add friend page
def add(request):
    if not request.session["logged_in"]:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    exclude = []
    friends = Friends.objects.all().filter(user__id=request.session["user_id"])
    for friend in friends:
        exclude.append(friend.friend.id)
    data = {
        "users": Users.objects.all().exclude(id=request.session["user_id"]).exclude(id__in=exclude),
    }
    return render(request, "friend_app/add.html", data)

# show user information
def user(request):
    if not request.session["logged_in"]:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    data = {
        "friends": Friends.objects.all().filter(user__id=request.session["user_id"]),
    }
    return render(request, "friend_app/user.html", data)

# adds new friendship
def new(request, id):
    if not request.session["logged_in"]:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    user = Users.objects.get(id=request.session["user_id"])
    friend = Users.objects.get(id=id)
    if len(Friends.objects.filter(user__id=request.session["user_id"]).filter(friend__id=id)) < 1:
        Friends.objects.create(user=user, friend=friend)
    else:
        messages.error(request, "Already friends.")
    return redirect("friend:add")

# deletes friendship
def delete(request, id):
    if not request.session["logged_in"]:
        messages.error(request, "Please log in.")
        return redirect("login:idx")
    Friends.objects.filter(user__id=request.session["user_id"]).filter(friend__id=id).delete()
    return redirect("friend:user")