from django.db import models

type_choice = (('Bookmark', 'Bookmark'), ('Folder', 'Folder'))


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Bookmark(models.Model):
    title = models.CharField(max_length=400)
    url = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag)
    type = models.CharField(max_length=100, choices=type_choice, default='Bookmark')
    parent = models.ForeignKey('Bookmark', null=True, on_delete=models.CASCADE)



