# Generated by Django 2.2 on 2020-08-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_remove_answers_qid'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='date',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
