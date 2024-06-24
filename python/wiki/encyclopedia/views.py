from random import choice  # Add this import statement

from django import forms
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.urls.exceptions import Http404
from markdown2 import Markdown

from . import util

markdowner = Markdown()


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


def random(request):

    entries = util.list_entries()
    print(entries)
    random_entry = choice(entries)
    print(random_entry)

    # Redirect to the page of the randomly chosen entry
    return HttpResponseRedirect(f"{random_entry}")


def show_entry(request, name):

    if check_exists(request, name) == False:
        return render(request, "encyclopedia/index.html", {"entries": "Not Found"})

    e = util.get_entry(name)

    f = markdowner.convert(e)

    return render(
        request,
        "encyclopedia/index.html",
        {"entries": f, "title": name.capitalize(), "isIndex": False},
    )


def add_entry(request):
    method = request.POST.get("_method", "").upper()
    form = NewEntryForm(request.POST)

    if request.method == "POST" and method == "PUT":
        print("method is post and put to update, handling it here .....")
        if form.is_valid():

            # 🐵 Convert the markdown back into HTML

            clean_title = form.cleaned_data["title"]
            clean_content = form.cleaned_data["content"]
            util.save_entry(clean_title, clean_content)
            return HttpResponseRedirect(f"{clean_title}")

    elif request.method == "POST":
        print("method is post only....")
        if form.is_valid():
            clean_title = form.cleaned_data["title"]
            clean_content = form.cleaned_data["content"]
            if check_exists(request, clean_title) == False:
                print("NEW ENTRY")
                util.save_entry(clean_title, clean_content)
                return HttpResponseRedirect(f"{clean_title}")
            else:
                messages.error(request, "This entry already exists.")
                return render(request, "encyclopedia/addentry.html", {"isError": True})

        else:
            print("FORM INVALID")

    else:
        print("Method is ???")

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


def edit(request, name):

    # Fetch the content using the get_entry function
    content = util.get_entry(name)

    # Convert into Markdown  🐵

    # Return the add_entry page with the content pre-loaded into the fields
    return render(
        request,
        "encyclopedia/addentry.html",
        {
            "isError": False,
            "isEdit": True,
            "title": name,
            "content": content,
        },
    )


## Functions for checking data. Should probably move to util.py


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
