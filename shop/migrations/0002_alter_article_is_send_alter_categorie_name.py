# Generated by Django 4.1.3 on 2023-03-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_send',
            field=models.BooleanField(default=False, help_text='  '),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('Vehicule', 'Vehicule'), ('Electronique', 'Electronique'), ('Immobilier', 'Immobilier'), ('Vetements', 'Vetements'), ('Animaux', 'Animaux'), ('Agriculture', 'Agriculture'), ('Bebe & Enfant', 'Bébé & Enfant')], max_length=255),
        ),
    ]
