# Generated by Django 4.0.4 on 2022-06-22 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_author_book_person_author_person_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Address_Line',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='Address_Line_2',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
