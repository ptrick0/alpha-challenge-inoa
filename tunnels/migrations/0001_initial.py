# Generated by Django 4.0.5 on 2022-06-28 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tunnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topLimit', models.FloatField()),
                ('bottomLimit', models.FloatField()),
                ('frequency', models.IntegerField()),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickers.ticker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]