from django import forms
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.urls.exceptions import Http404

from . import util


class NewEntryForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(label="content")


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
    if request.method == "POST":

        form = NewEntryForm(request.POST)
        if form.is_valid():
            clean_title = form.cleaned_data["title"]
            clean_content = form.cleaned_data["content"]
            if check_exists(request, clean_title) == False:
                util.save_entry(clean_title, clean_content)
                ## This is a terrible way of displaying the new entry, you should just re-route to the title name
                ## but you'll need to write a function to account for spaces.

                ## TODO 🐵 .............  wiki is not a namespace???
                return HttpResponseRedirect(reverse("wiki:index"))

            else:
                print("THIS ENTRY ALREADY EXISTS")
        else:
            print("FORM INVALID")
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
