# Generated by Django 5.1.7 on 2025-03-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0004_signtypinggame_alter_leaderboard_game_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='game_type',
            field=models.CharField(choices=[('quiz', 'Quiz'), ('word_match', 'Word Match'), ('flashcard', 'Flashcard'), ('sign_typing_game', 'Sign Typing Game')], default='quiz', max_length=20),
        ),
    ]
