from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
import markdown2
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "titles": util.list_entries()
    })


# my code
def send_entry(request, title):
    data = util.get_entry(title)
    if data is None:
        raise Http404('Page not found')
    return render(request, "encyclopedia/entry.html", {
        "title": data[0],
        "entry": markdown2.markdown(data[1])
    })


def send_search(request):
    search = request.GET.get('q', '')
    data = util.get_entry(search)
    if data is not None:
        # отправляем html-страницу искомой статьи
        # return render(request, "encyclopedia/entry.html", {
        #     'title': data[0],
        #     'entry': markdown2.markdown(data[1])
        # })
        return redirect(f'/{data[0]}')
    else:
        search_results = []
        entries_list = util.list_entries()
        for title in entries_list:
            if search.lower() in title.lower():
                search_results.append(title)
        return render(request, "encyclopedia/search.html", {
            "search_results": search_results,
            "search_request": search
        })


def new_page(request):
    if request.method == 'POST':
        # если статья с таким заголовком уже есть
        data = util.get_entry(request.POST['title'])
        if data is not None:
            return render(request, "encyclopedia/newpage.html", {
            "error": True
            })
        else:
            util.save_entry(request.POST['title'], request.POST['content'])
            # return render(request, "encyclopedia/entry.html", {
            #     'title': request.POST['title'],
            #     'entry': markdown2.markdown(request.POST['content'])
            # })
            return redirect(f"/{request.POST['title']}")
    # если не POST-метод
    return render(request, "encyclopedia/newpage.html")


def edit_page(request, title):
    if request.method == "POST":
        util.save_entry(title, request.POST['content'])
        return redirect(f"/{title}")

    return render(request, "encyclopedia/editpage.html", {
        'title': title,
        'entry': util.get_entry(title)[1]
    })


