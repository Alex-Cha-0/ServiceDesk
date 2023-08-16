from django.core.management.base import BaseCommand
from applications.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        cat = Category.objects.get(ordernumber__category=1560)
        print(cat)
