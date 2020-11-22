from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import markdown2

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
        return render(request, "encyclopedia/entry.html", {
            'title': data[0],
            'entry': markdown2.markdown(data[1])
        })
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

# def test_func(request):
#     return HttpResponse("Test")
