from django.core.management.base import BaseCommand
from faker import Faker

import customauth.models
from customauth.models import MyUser


def populate_players(self, N):
    faker = Faker()
    self.stdout.write(self.style.SUCCESS('creating players'))
    for i in range(N):
        username = faker.unique.user_name()
        password = faker.lexify(text='??????????')
        MyUser.objects.create_user(
            username,
            password,
            faker.unique.email(),
            faker.date(),
            faker.first_name(),
            faker.last_name(),
            customauth.models.USER_TYPE_PLAYER,
            faker.random_int(min=150, max=250),
            i % 16 + 1
        )

        self.stdout.write(self.style.SUCCESS('Username : "%s" Password : "%s"' % (username, password)))
    self.stdout.write(self.style.SUCCESS('players created successfully'))
    pass


def populate_coaches(self, N):
    faker = Faker()
    self.stdout.write(self.style.SUCCESS('creating coaches'))
    for i in range(N):
        username = faker.unique.user_name()
        password = faker.lexify(text='??????????')
        MyUser.objects.create_user(
            username,
            password,
            faker.unique.email(),
            faker.date(),
            faker.first_name(),
            faker.last_name(),
            customauth.models.USER_TYPE_COACH,
            faker.random_int(min=150, max=250),
            i % 16 + 1
        )
        self.stdout.write(self.style.SUCCESS('Username : "%s" Password : "%s"' % (username, password)))
    self.stdout.write(self.style.SUCCESS('coaches created successfully'))
    pass


def create_admin(self, N):
    faker = Faker()
    self.stdout.write(self.style.SUCCESS('creating admin'))

    for i in range(N):
        username = 'sadmin'
        password = 'sadmin@123'
        MyUser.objects.create_user(
            username,
            password,
            faker.unique.email(),
            faker.date(),
            faker.first_name(),
            faker.last_name(),
            customauth.models.USER_TYPE_ADMIN,
            faker.random_int(min=150, max=250),
            None
        )

        self.stdout.write(self.style.SUCCESS('Username : "%s" Password : "%s"' %(username,password)))
    self.stdout.write(self.style.SUCCESS('Admin created successfully'))
    pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_admin(self,N=1)
        populate_coaches(self, N=16)
        populate_players(self, N=160)

        self.stdout.write(self.style.SUCCESS('Successful'))
