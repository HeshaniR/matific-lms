from django.db import models


class TeamManager(models.Manager):

    def get_teams(self):
        """Fetch Team Details
        @return: return team : List[MyUser]"""
        return list(Team.objects.values())

    def get_team_by_id(self, team_id):
        """
        Fetch team Details by team_id
        @param team_id:
        @return: return teams : List[MyUser]
        """
        return Team.objects.get(id=team_id)

    def create_team(self, name):
        team = self.model(
            name=name
        )
        team.save(using=self._db)
        return team


class Team(models.Model):
    name = models.CharField(max_length=200)

    objects = TeamManager()
