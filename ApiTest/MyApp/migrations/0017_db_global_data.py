# Generated by Django 3.1.3 on 2021-03-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0016_db_step_api_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_global_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('user_id', models.CharField(max_length=20, null=True)),
                ('data', models.TextField(null=True)),
            ],
        ),
    ]