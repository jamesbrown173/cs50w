from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls.exceptions import Http404

from . import util


def index(request):
    return render(
        request,
        "encyclopedia/index.html",
        {"entries": util.list_entries(), "isIndex": True},
    )


def show_entry(request, name):

    if check_exists(request, name) == False:
        return render(request, "encyclopedia/index.html", {"entries": "Not Found"})

    e = util.get_entry(name)

    return render(
        request,
        "encyclopedia/index.html",
        {"entries": e, "title": name.capitalize(), "isIndex": False},
    )


def check_exists(request, name):
    entries = util.list_entries()
    lower_n = name.lower()
    lower_e = [entry.lower() for entry in entries]
    if lower_n not in lower_e:
        return False
