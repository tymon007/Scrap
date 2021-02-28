# Generated by Django 3.1.7 on 2021-02-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_auto_20210228_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='rekord',
            name='kod_odpadu',
            field=models.IntegerField(default=0, help_text='It is numeric representation of waga'),
        ),
        migrations.AddField(
            model_name='rekord',
            name='nazwa_metalu',
            field=models.TextField(default='', help_text="It is text describing user's problem here"),
        ),
    ]