# Generated by Django 3.1.2 on 2021-09-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0045_auto_20210914_1538"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item_match_performance",
            name="summonerId",
            field=models.CharField(max_length=100, null=True),
        ),
    ]