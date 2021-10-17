from django.db import models

# Create your models here.
from django.db.models import Count

from customauth.models import MyUser
from team.models import Team


class GameActivityManager(models.Manager):

    def get_team_scores(self, team_id):
        """
        Retrieve the team Scores
        @param team_id: int
        @return: team_id, activity,  activity_count
        """
        return GameActivity.objects.filter(team_id=team_id).values('team_id', 'activity').annotate(
            activity_count=Count('activity'))

    def get_player_scores(self, player_id):
        """
         Retrieve the player Scores
        @param player_id:
        @return: player_id, activity,  activity_count
        """
        return GameActivity.objects.filter(player_id=player_id).values('player_id', 'activity').annotate(
            activity_count=Count('activity'))

    def create_game_activity(self,game_id,player_id,team_id,activity=1):
        game_activity = self.model(
            game_id = game_id,
            player_id = player_id,
            team_id = team_id,
            activity = activity
        )

        game_activity.save(using= self._db)
        return game_activity

class GameManager(models.Manager):

    def create_game(self, name, team_one, team_two, round = 1, status = 1,
                     team_one_score = 0, team_two_score = 0, winning_team_id = None):
        game = self.model(
            name=name,
            team_one_id=team_one,
            team_two_id=team_two,
            round = round,
            status = status,
            team_one_score = team_one_score,
            team_two_score = team_two_score,
            winning_team_id = winning_team_id
        )
        game.save(using=self._db)
        return game


class Game(models.Model):
    name = models.CharField(max_length=200)
    team_one = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='team_one', null=True)
    team_two = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='team_two', null=True)
    winning_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='winning_team', null=True)
    team_one_score = models.PositiveIntegerField(default=0)
    team_two_score = models.PositiveIntegerField(default=0)
    status = models.PositiveIntegerField(default=0)
    round = models.PositiveIntegerField(default=0)

    objects = GameManager()


class GameActivity(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    activity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    objects = GameActivityManager()


STATUS_SCHEDULED = 1
STATUS_STARTED = 2
STATUS_END = 3

ACTIVITY_IS_TRY = 0
ACTIVITY_IS_GOAL = 1
