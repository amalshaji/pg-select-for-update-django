from django.core.management.base import BaseCommand

from journey.models import Journey


class Command(BaseCommand):
    help = "Start journey start node creator"

    def handle(self, *args, **options):
        Journey.objects.bulk_create([Journey() for _ in range(13)])
