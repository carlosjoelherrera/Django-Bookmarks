from django.urls import path

from core.views import BookmarkList, BookmarkCreate

urlpatterns = [
    path('', BookmarkList.as_view(), name='list'),
    path('new/', BookmarkCreate.as_view(), name='create')
]
