# Generated by Django 3.2 on 2021-09-07 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='active',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='avaliacao',
            old_name='comment',
            new_name='comentario',
        ),
        migrations.RenameField(
            model_name='avaliacao',
            old_name='created',
            new_name='criado',
        ),
        migrations.RenameField(
            model_name='avaliacao',
            old_name='course',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='avaliacao',
            old_name='modified',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='avaliacao',
            old_name='username',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='active',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='created',
            new_name='criado',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='title',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='modified',
            new_name='modificado',
        ),
        migrations.AlterUniqueTogether(
            name='avaliacao',
            unique_together={('email', 'curso')},
        ),
    ]
