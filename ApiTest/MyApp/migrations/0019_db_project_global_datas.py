# Generated by Django 3.1.3 on 2021-04-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0018_db_project_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_project',
            name='global_datas',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
