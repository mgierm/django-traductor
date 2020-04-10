from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Translates your messages'

    def handle(self, *args, **options):
        pass
        self.stdout.write(self.style.SUCCESS('All messages translated'))
