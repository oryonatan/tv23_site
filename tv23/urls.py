from django.conf.urls import include, url
from django.contrib import admin
import video.views


# delte me please
urlpatterns = [
    url(r'^$', video.views.SeriesListView.as_view(), name="main"),

    # url(r'^r/',video.views.view_random_video),
    url(r'^series/$', video.views.SeriesListView.as_view(), name="series_list"),
    url(r'^series/(?P<pk>\d+)$', video.views.SeriesDetailView.as_view(), name="series"),

    url(r'^genre/$', video.views.GenreListView.as_view(), name="genre_list"),
    url(r'^genre/(?P<pk>\d+)$', video.views.GenreDetailView.as_view(), name="genre"),

    url(r'^tag/$', video.views.TagListView.as_view(), name="tag_list"),
    url(r'^tag/ajax/$', video.views.TagListAjaxView.as_view(), name="tag_list_ajax"),
    url(r'^tag/(?P<pk>\d+)$', video.views.TagDetailView.as_view(), name="tag"),

    url(r'^all/$',video.views.AssetListView.as_view(),name="video_list"),
    url(r'^search/$',video.views.AssetSearchView.as_view(),name="video_search"),
    url(r'^(?P<pk>\d+)/$', video.views.AssetDetailView.as_view(), name="video"),

    url(r'^admin/', include(admin.site.urls)),
]
