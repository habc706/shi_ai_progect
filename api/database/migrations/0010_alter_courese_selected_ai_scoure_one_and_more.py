# Generated by Django 4.0a1 on 2021-11-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_wuser_info_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courese_selected',
            name='ai_scoure_one',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='courese_selected',
            name='cou_se_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='courese_selected',
            name='scoure_one',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='course',
            name='cou_info',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]