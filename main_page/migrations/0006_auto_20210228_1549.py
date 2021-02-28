# Generated by Django 3.1.7 on 2021-02-28 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_auto_20210228_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='kod_odpadu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('opis', models.TextField(help_text="It is text describing user's problem here")),
            ],
        ),
        migrations.AlterField(
            model_name='rekord',
            name='kod_odpadu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.kod_odpadu'),
        ),
    ]