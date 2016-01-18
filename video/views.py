from django import forms
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from . import models
from django.views.generic.base import View

import taggit.models


class SnippetForm(forms.ModelForm):
    class Meta:
        model = models.Snippet
        fields = (
            'start_time',
            'end_time',
            'title',
            'description',
            'tags',
        )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("start_time") >= cleaned_data.get("end_time"):
            raise forms.ValidationError(
                    "start time must be smaller than end time")


class AssetDetailView(DetailView):
    model = models.Asset

    def get_title(self):
        return self.object

    def empty_form(self):
        return SnippetForm()

    def post(self, request, *args, **kwargs):
        form = SnippetForm(data=request.POST)
        if not form.is_valid():
            return JsonResponse(
                    {'result': "bad data", 'errors': form.errors.as_json()},
                    status=400)
        form.instance.asset = self.get_object()
        form.save()
        return render(request, "video/_snippet.html", {
            'snippet': form.instance,
        })


class AssetListView(ListView):
    model = models.Asset
    paginate_by = 60
    ordering = "?"


class SeriesListView(ListView):
    model = models.Series
    paginate_by = 36
    queryset = models.Series.objects.order_by("name")


class SeriesDetailView(DetailView):
    model = models.Series


class SeasonDetailView(DetailView):
    model = models.Season


class GenreListView(ListView):
    model = models.Genre
    ordering = "name"


class GenreDetailView(DetailView):
    model = models.Genre


class TagListView(ListView):
    model = taggit.models.Tag


class TagDetailView(DetailView):
    model = taggit.models.Tag


class TagListAjaxView(View):
    def get(self, request, *args, **kwargs):
        qs = taggit.models.Tag.objects.order_by('name')
        return JsonResponse([{'id': tag.name, 'text': tag.name} for tag in qs],
                            safe=False)
