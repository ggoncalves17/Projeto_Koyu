# Generated by Django 5.1.3 on 2024-12-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetoKoyu_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilizador',
            old_name='ut_pass',
            new_name='password',
        ),
        migrations.AddField(
            model_name='utilizador',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='utilizador',
            name='ut_mail',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
