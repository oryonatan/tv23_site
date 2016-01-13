import argparse
import json

from django.core.management.base import BaseCommand
from tqdm import tqdm

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

        for asset in tqdm(assets):
            self.import_asset(asset)
        print("Done.")

    def import_asset(self, asset):
        genres = [models.Genre.objects.get_or_create(name=genere_name)[0] for
                  genere_name in asset['genres']]

        asset['series'], created = models.Series.objects.get_or_create(
                name=asset['series']
        )

        asset['year'] = asset['year'] or 1
        season, created = models.Season.objects.get_or_create(
                series=asset['series'],
                year=asset['year']
        )

        if asset['episode'].isnumeric():
            asset['episode'] = int(asset['episode']) or 999999
        else:
            asset['episode'] = 999999

        del asset['genres']

        o = models.Asset.objects.create(
                season=season,
                **asset
        )
        o.genres.add(*genres)
        o.save()
