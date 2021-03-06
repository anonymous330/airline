# Generated by Django 3.0 on 2019-12-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20191213_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passenger', to='flights.flight')),
            ],
        ),
    ]
