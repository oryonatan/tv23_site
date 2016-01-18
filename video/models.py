from django.core.urlresolvers import reverse
from django.db import models
from taggit.managers import TaggableManager

THUMBNAIL_URL = 'http://cdnbakmi.kaltura.com/p/1829221/sp/182922100/thumbnail/entry_id/{}/version/100000/acv/161'

KALTURA_DYNAMIC_EMBED = """http://cdnapi.kaltura.com/p/{PARTNER_ID}/sp/{PARTNER_ID}00/embedIframeJs/uiconf_id/{UICONF_ID}/partner_id/{PARTNER_ID}?entry_id={ENTRY_ID}&playerId={UNIQUE_OBJ_ID}&cache_st=1362074486&autoembed=true&width=400&height=333&"""
KALTURA_DYNAMIC_EMBED = KALTURA_DYNAMIC_EMBED.replace("{PARTNER_ID}",
                                                      "1829221") \
    .replace("{UICONF_ID}", "28733761") \
    .replace("{UICONF_ID}", "28733761") \
    .replace("{UNIQUE_OBJ_ID}", "KalturaDynamicPlayer")


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.strip() or "kuku"

    def get_absolute_url(self):
        return reverse("genre", args=(self.pk,))


class Series(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    # from_year = models.SmallIntegerField(null=True)
    # to_year = models.SmallIntegerField(null=True)
    genre = models.ManyToManyField(Genre, related_name="appears_in_series",
                                   blank=True)
    # TODO : add link to image

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    def thumbnail(self):
        return self.asset_set.first().get_thumbnail_url()

    def get_absolute_url(self):
        return reverse("series", args=(self.id,))

    def assets_by_epiosde(self):
        return self.asset_set.order_by("episode")


class Season(models.Model):
    series = models.ForeignKey(Series)
    year = models.SmallIntegerField(null=True)

    def __str__(self):
        return str(self.year)

    def get_ordered_assets(self):
        return self.asset_set.order_by("episode")

    def get_absolute_url(self):
        return reverse("season", args=(self.id,))


class Asset(models.Model):
    entry_id = models.CharField(max_length=50, unique=True)
    durationms = models.PositiveIntegerField(null=True)
    system_id = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    series = models.ForeignKey(Series, null=True)
    season = models.ForeignKey(Season, null=True)
    episode = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    synopsys = models.CharField(max_length=200)
    audience = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre, related_name="appears_in_assets",
                                    blank=True)
    primo_url = models.CharField(max_length=200)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("video", args=(self.id,))

    def get_dynamic_embed_script(self):
        return KALTURA_DYNAMIC_EMBED.replace("{ENTRY_ID}", self.entry_id)

    def get_thumbnail_url(self):
        return THUMBNAIL_URL.format(self.entry_id)


class Snippet(models.Model):
    asset = models.ForeignKey(Asset, related_name='snippets')
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    tags = TaggableManager(blank=True)

    def duration(self):
        return self.end_time - self.start_time

    def get_kaltura_thumb_start_offset(self):
        ratio = self.start_time / (self.asset.durationms / 1000)
        return str(int(ratio * 10000 // 100 * 100 - 100))

    def get_kaltura_thumb_end_offset(self):
        ratio = self.end_time / (self.asset.durationms / 1000)
        return str(int(ratio * 10000 // 100 * 100 - 100))
