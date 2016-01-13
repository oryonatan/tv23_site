import random

from django import forms
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from . import models
# Create your views here.
from django.views.generic.base import View


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

    def kuku(self):
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
    def get_queryset(self):
        EPISODES_PER_PAGE = int(self.kwargs['ep_per_page'])
        first_ep = (int(self.kwargs['page']) - 1) * EPISODES_PER_PAGE
        last_ep = first_ep + EPISODES_PER_PAGE
        series = models.Series.objects.get(pk=self.kwargs['pk'])
        return series.asset_set.order_by("episode").all()[first_ep:last_ep]


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


class GenreDetailView(DetailView):
    model = models.Genre
