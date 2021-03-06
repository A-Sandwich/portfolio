# Generated by Django 3.1.3 on 2020-11-25 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('details', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('completed', models.BooleanField()),
            ],
        ),
    ]
