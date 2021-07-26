# Generated by Django 2.2 on 2021-07-23 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0009_auto_20210714_2224'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='hashtag',
            index_together={('hashtag', 'rev_id'), ('hashtag', 'domain', 'page_title'), ('hashtag', 'username'), ('hashtag', 'timestamp')},
        ),
    ]
