from django.conf.urls import include, url
from django.contrib import admin
import video.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', video.views.SeriesListView.as_view(), name="main"),
    # url(r'^r/',video.views.view_random_video),
    url(r'^(?P<pk>\d+)/$', video.views.AssetDetailView.as_view(), name="video"),
    # url(r'^$',video.views.AssetListView.as_view(),name="home"),
    url(r'^ser/(?P<pk>\d+)/(?P<ep_per_page>\d+)/(?P<page>\d+)$', video.views.AssetListView.as_view(),
        name="episodes_list"),
    url(r'^ser/$', video.views.SeriesListView.as_view(), name="series_list"),
    url(r'^ser/(?P<pk>\d+)$', video.views.SeriesDetailView.as_view(), name="series"),
    url(r'^sea/(?P<pk>\d+)$', video.views.SeasonDetailView.as_view(), name="season"),
    url(r'^gen/$', video.views.GenreListView.as_view(), name="genre_list"),
    url(r'^gen/(?P<pk>\d+)$', video.views.GenreDetailView.as_view(), name="genre"),
    url(r'^tag/$', video.views.TagListView.as_view(), name="tag_list"),
    url(r'^tag/ajax/$', video.views.TagListAjaxView.as_view(), name="tag_list_ajax"),
    url(r'^tag/(?P<pk>\d+)$', video.views.TagDetailView.as_view(), name="tag"),
]
