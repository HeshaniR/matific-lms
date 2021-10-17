from django.core.management.base import BaseCommand
from faker import Faker

from team.models import Team


def populate_teams(self, N):
    faker = Faker()

    for i in range(N):
        Team.objects.create_team(faker.country())
    pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        populate_teams(self, N=16)

        self.stdout.write(self.style.SUCCESS('Successful'))

