# Generated by Django 2.0.1 on 2018-03-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_auto_20180315_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='action',
            field=models.CharField(choices=[('S', 'Snack'), ('P', 'Play'), ('O', 'Outside'), ('B', 'Bathroom'), ('CH', 'CallHome'), ('N', 'Nurse'), ('R', 'Read')], max_length=1),
        ),
    ]
