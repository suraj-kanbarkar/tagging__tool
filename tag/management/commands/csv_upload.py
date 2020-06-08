from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
import csv
# from tt2.tag.models import *
from tag.models import TagData
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('/home/appdevelopement/Desktop/sel.csv', 'rt') as file:
            reader = csv.DictReader(file, delimiter=',')
            csv_data = list(reader)
            for i in csv_data:
                f = TagData(text=i['data'].encode('ascii', 'ignore').decode('ascii'))
                f.save()
                print(i['data'])