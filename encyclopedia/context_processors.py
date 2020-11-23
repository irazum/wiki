from . import util
from random import choice


def random_page(request):
    titles = util.list_entries()
    return {"context_random_page": choice(titles) if titles else ""}
