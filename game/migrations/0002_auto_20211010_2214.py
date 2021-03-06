# Generated by Django 3.2.8 on 2021-10-10 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_remove_team_score'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='score',
            new_name='round',
        ),
        migrations.RemoveField(
            model_name='game',
            name='team',
        ),
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='team_one',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='team_one', to='team.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_one_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='team_two',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='team_two', to='team.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_two_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='winning_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='winning_team', to='team.team'),
        ),
        migrations.CreateModel(
            name='GameActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
    ]
