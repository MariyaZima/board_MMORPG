# Generated by Django 5.0.6 on 2024-06-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('tanks', 'Танки'), ('frail', 'Хилы'), ('dd', 'ДД'), ('merchants', 'Торговцы'), ('guild_masters', 'Гилдмастеры'), ('quest_givers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potion_makers', 'Зельевары'), ('spell_masters', 'Гилдмастеры')], max_length=15, verbose_name='Категория'),
        ),
    ]
