from django.views.generic import ListView, CreateView, UpdateView

from core.models import Bookmark


class BookmarkFolderCreate(CreateView):
    model = Bookmark
    fields = ['title']


class BookmarkList(ListView):
    model = Bookmark
    fields = ['title', 'url']


class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['title', 'url', 'type']
    success_url = '/'


class BookmarkUpdate(UpdateView):
    model = Bookmark
