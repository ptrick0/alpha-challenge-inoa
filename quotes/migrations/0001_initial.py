# Generated by Django 4.0.5 on 2022-06-28 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moment', models.DateTimeField()),
                ('value', models.FloatField()),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickers.ticker')),
            ],
        ),
    ]