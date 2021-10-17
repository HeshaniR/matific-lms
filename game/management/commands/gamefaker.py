from django.core.management.base import BaseCommand
from faker import Faker

import game.models
from game.models import Game, GameActivity


def populate_games(self, N):
    faker = Faker()

    for i in range(N):
        status = faker.random_int(min=1, max=3)

        if status == game.models.STATUS_SCHEDULED:
            team_one_score = 0
            team_two_score = 0
            winning_team = None
        if status == game.models.STATUS_STARTED:
            team_one_score = faker.random_int(min=1, max=100)
            team_two_score = faker.random_int(min=1, max=100)
            winning_team = None
        if status == game.models.STATUS_END:
            team_one_score = faker.random_int(min=1, max=100)
            team_two_score = faker.random_int(min=1, max=100)
            if team_one_score > team_two_score:
                winning_team = i * 2 + 1
            else:
                winning_team = i * 2 + 2
        Game.objects.create_game(
            name='Game ' + str(i),
            team_one=i * 2 + 1,
            team_two=i * 2 + 2,
            team_one_score=team_one_score,
            team_two_score=team_two_score,
            winning_team_id=winning_team,
            round=1,
            status=status
        )
        pass


def populate_game_activities(self, N):
    faker = Faker()

    for i in range(N):
        GameActivity.objects.create_game_activity(
            game_id=i % 8 + 1,
            player_id=faker.random_int(min=1, max=160),
            team_id=faker.random_int(min=1, max=16),
            activity=faker.random_int(min=0, max=1),
        )
        pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        populate_games(self, N=8)
        populate_game_activities(self, N=300)

        self.stdout.write(self.style.SUCCESS('Successful'))
