# Generated by Django 5.0.3 on 2024-03-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_loaninformations_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='capa_livro'),
        ),
    ]
