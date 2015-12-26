from django.core.urlresolvers import reverse
from django.db import models
KALTURA_DYNAMIC_EMBED = """http://cdnapi.kaltura.com/p/{PARTNER_ID}/sp/{PARTNER_ID}00/embedIframeJs/uiconf_id/{UICONF_ID}/partner_id/{PARTNER_ID}?entry_id={ENTRY_ID}&playerId={UNIQUE_OBJ_ID}&cache_st=1362074486&autoembed=true&width=400&height=333&"""
KALTURA_DYNAMIC_EMBED = KALTURA_DYNAMIC_EMBED.replace("{PARTNER_ID}","1829221")\
    .replace("{UICONF_ID}","28733761")\
    .replace("{UICONF_ID}","28733761")\
    .replace("{UNIQUE_OBJ_ID}","KalturaDynamicPlayer")


class Genre(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name



class Series(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    # from_year = models.SmallIntegerField(null=True)
    # to_year = models.SmallIntegerField(null=True)
    genre = models.ManyToManyField(Genre,related_name="appears_in_series",blank=True)
    '''todo : add link to image   '''
    def __str__(self):
        return self.name
    def thumbnail(self):
        return self.asset_set.first().thumbnail_url
    def get_absolute_url(self):
        return reverse("series",args=(self.id,))



class Season(models.Model):
    series = models.ForeignKey(Series)
    year = models.SmallIntegerField(null=True)

    def __str__(self):
        return str(self.year)

    def get_ordered_assets(self):
        return self.asset_set.order_by("episode")

    def get_absolute_url(self):
        return reverse("season",args=(self.id,))



class Asset(models.Model):
    system_id = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    series = models.ForeignKey(Series,null=True)
    season = models.ForeignKey(Season,null=True)
    episode = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    synopsys = models.CharField(max_length=200)
    audience = models.CharField(max_length=200,null=True)
    genres = models.ManyToManyField(Genre,related_name="appears_in_assets",blank=True)
    primo_url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200)
    entry_id = models.CharField(max_length=50)
    video_url = models.CharField(max_length=300)
    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("video",args=(self.id,))

    def get_dynamic_embed_script(self):
        return KALTURA_DYNAMIC_EMBED.replace("{ENTRY_ID}",self.entry_id)
