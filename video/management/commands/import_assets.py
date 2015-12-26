import argparse
import json
from pprint import pprint
from django.core.management.base import BaseCommand, CommandError
from video import models

NLI_PARTNER_ID = """1829221"""


class Command(BaseCommand):
    help = 'Imports assets from assets.json'

    def add_arguments(self, parser):
        parser.add_argument('infile', type=argparse.FileType('r'),
                            help="path to assets_file.json")

    def handle(self, *args, **options):
        assets = json.load(options['infile'])
        self.stdout.write("{} assets found.".format(len(assets)))

        for asset in assets:
            try:
                self.import_asset(asset)
            except Exception as e:
                print(e)

    def import_asset(self, asset):
        genres = [models.Genre.objects.get_or_create(name=genere_name)[0] for genere_name in asset['genres']]

        series, created = models.Series.objects.get_or_create(
            name=asset['series']
        )

        fixed_year = asset['year'] or 1
        season, created = models.Season.objects.get_or_create(
            series=series,
            year=fixed_year
        )
        try:
            episode = int(asset['episode']) or 999999
        except Exception:
            episode = 999999

        theAsset, created = models.Asset.objects.get_or_create(
            system_id=asset['system_id']
        )
        theAsset.year = fixed_year,
        theAsset.series = series,
        theAsset.season = season,
        theAsset.episode = episode,
        theAsset.title = asset['title'],
        theAsset.full_name = asset['full_name'],
        theAsset.language = asset['language'],
        theAsset.synopsys = asset['synopsys'],
        theAsset.audience = asset['audience'],
        theAsset.primo_url = asset['primo_url'],
        theAsset.thumbnail_url = asset['thumbnail_url'],
        theAsset.entry_id = asset['entry_id'],
        theAsset.video_url_iframe = asset['video_url'],
        theAsset.genres.add(*genres)
        theAsset.save()
