# Generated by Django 3.1.3 on 2021-03-12 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0017_db_global_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_project',
            name='user_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]