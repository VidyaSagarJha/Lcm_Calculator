# Generated by Django 3.2 on 2021-05-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lcm_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputEnter', models.CharField(max_length=250)),
                ('detailStep', models.TextField()),
                ('finalAnswer', models.CharField(max_length=1000)),
                ('slug', models.CharField(max_length=300)),
                ('solutionTitle', models.CharField(max_length=250)),
                ('date_modified', models.DateTimeField()),
            ],
        ),
    ]
