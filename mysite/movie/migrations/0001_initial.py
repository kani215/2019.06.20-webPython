# Generated by Django 2.2 on 2019-05-27 11:18

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieId', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('movieName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ScreenTime',
            fields=[
                ('screenId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('screenDate', models.DateField()),
                ('screenTime', models.TimeField()),
                ('movieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatRow', models.IntegerField()),
                ('seatCol', models.CharField(max_length=3)),
                ('status', models.BooleanField(default=False)),
                ('screenId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.ScreenTime')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservationId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('movieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('screenId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.ScreenTime')),
                ('seatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Seat')),
                ('username', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]