import argparse
import json
import csv
from django.core.management.base import BaseCommand
from tqdm import tqdm

from video import models


class Command(BaseCommand):
    help = 'Fix assets durations from csv '

    def add_arguments(self, parser):
        parser.add_argument('infile', type=argparse.FileType('r'),
                            help="path to durations.csv")

    def handle(self, *args, **options):
        change_count = 0
        times = csv.reader(options['infile'])
        for entry_id,durationms in tqdm(times):
            change_count  += models.Asset.objects.filter(entry_id=entry_id).update(durationms=durationms)
        print("{} durations updated".format(change_count))