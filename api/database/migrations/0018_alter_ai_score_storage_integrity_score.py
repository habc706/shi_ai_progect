# Generated by Django 4.0a1 on 2021-11-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_ai_score_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ai_score_storage',
            name='integrity_score',
            field=models.FloatField(default='', max_length=15),
        ),
    ]