# Generated by Django 3.1.4 on 2021-12-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codechef', '0003_remove_codechefcontestproblems_problemid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codechefcontest',
            name='division',
        ),
        migrations.AlterField(
            model_name='codechefcontest',
            name='startTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
