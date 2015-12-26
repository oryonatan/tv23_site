import random
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from . import models
# Create your views here.
from django.views.generic.base import View


class AssetDetailView(DetailView):
    model = models.Asset


class AssetListView(ListView):
    def get_queryset(self):
        EPISODES_PER_PAGE = int(self.kwargs['ep_per_page'])
        first_ep = (int(self.kwargs['page'])-1) * EPISODES_PER_PAGE
        last_ep= first_ep + EPISODES_PER_PAGE
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


class GenreDetailView(DetailView):
    model = models.Season
