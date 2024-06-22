from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls.exceptions import Http404

from . import util


def index(request):
    query = request.GET.get("q")
    if query:
        return search(request, query)

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


def add_entry(request):
    return render(request, "encyclopedia/addentry.html")


def search(request, query):
    entries = util.list_entries()
    lower_query = query.lower()

    matching_entries = [entry for entry in entries if lower_query in entry.lower()]

    if matching_entries:
        return render(
            request,
            "encyclopedia/index.html",
            {"entries": matching_entries, "query": query, "isIndex": True},
        )
    else:
        return render(
            request,
            "encyclopedia/index.html",
            {
                "entries": "Not matching results",
                "query": query,
                "not_found": True,
            },
        )


def check_exists(request, name):
    entries = util.list_entries()
    lower_n = name.lower()
    lower_e = [entry.lower() for entry in entries]
    return lower_n in lower_e


def partial_match(request, name):
    entries = util.list_entries()
    lower_n = name.lower()
    lower_e = [entry.lower() for entry in entries]
    return any(lower_n in entry for entry in lower_e)
