from datetime import datetime

from django.contrib.auth.hashers import check_password
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

import customauth
from team.models import Team


class MyUserManager(BaseUserManager):
    def create_user(self, username, password, email, date_of_birth, first_name, last_name, user_type=None, height=None,
                    team_id=None):
        """
        create the user
        @param username:
        @param password:
        @param email:
        @param date_of_birth:
        @param first_name:
        @param last_name:
        @param user_type:
        @param height:
        @param team_id:
        @return: user :MyUser
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('Users must have a password')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not date_of_birth:
            raise ValueError('Users must have a DOB')

        user = self.model(
            email=self.normalize_email(email),
            username=username.lower(),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            height=height,
            user_type=user_type,
            team_id=team_id
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def authenticate(self,username, password):
        """
        Get authenticate User
        @param username: str
        @param password: str
        @return: user :MyUser
        """
        user = MyUser.objects.get(username=username)
        if not check_password(password, user.password):
            raise ValueError('Username of password is incorrect')
        return user

    def get_player_by_id(self, player_id,request):
        """
        Retrieve the player from DB by player id
        @param player_id:
        @param request:
        @return: data,message, status
        """
        player = MyUser.objects.get(id=player_id)
        if request.user.user_type == customauth.models.USER_TYPE_PLAYER and request.user.id != player.id:
            message = 'Players are not allowed to view other players info'
            return None, message, False
        elif request.user.user_type == customauth.models.USER_TYPE_COACH and request.user.team_id != player.team_id:
            message = 'coach is not allowed to view other Team players info'
            return None, message, False
        else:
            message = 'Player fetched successfully'
            data = {
                'first_name': player.first_name ,
                'last_name': player.last_name,
                'height': player.height,
                'date_of_birth': player.date_of_birth,
                'team': player.team.name if player.team is not None else '',
                'type': customauth.models.USER_TYPE_PLAYER,
            }
            return data, message, True

    def get_players(self, request):
        """
        Retrieve all players from DB
        @param request:
        @return: players
        """
        if request.user.user_type == customauth.models.USER_TYPE_COACH:
            message = 'Your players were fetched successfully'
            return list(MyUser.objects.filter(team_id=request.user.team_id, team_id__isnull=False).exclude(
                id=request.user.id).values('id','first_name','last_name','height','date_of_birth','team_id')), message, True
        elif request.user.user_type == customauth.models.USER_TYPE_PLAYER:
            message = 'You are not allowed to see the player list'
            return None, message, False
        else:
            message = 'All players were fetched successfully'
            return list(MyUser.objects.filter(user_type=customauth.models.USER_TYPE_PLAYER).exclude(
                id=request.user.id).values('id','first_name','last_name','height','date_of_birth','team_id')), message, True

    def get_user_stats(self):
        """Get the statistics of the user regarding login"""
        return list(MyUser.objects.values('first_name', 'login_count'))


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.EmailField(
        max_length=55,
        unique=True,
    )
    USER_TYPES = [(1,'admin'),(2,'coach'),(3,'player')]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    login_time = models.DateTimeField(null=True)
    time_spent = models.BigIntegerField(default= 0, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_type = models.IntegerField(choices=USER_TYPES, default=3)
    height = models.FloatField(default=0)
    login_count = models.PositiveIntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, default=None, null=True, related_name ='my_users')

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


USER_TYPE_ADMIN = 1
USER_TYPE_COACH = 2
USER_TYPE_PLAYER = 3
