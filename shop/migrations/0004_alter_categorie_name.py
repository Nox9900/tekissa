# Generated by Django 4.1.3 on 2023-03-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_article_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('Véhicule', 'Véhicule'), ('Electronique', 'Electronique'), ('Immobilier', 'Immobilier'), ('Vetements', 'Vetements'), ('Accessoires', 'Accessoires'), ('Animaux', 'Animaux'), ('Autres', 'Autres')], default='Autres', max_length=255),
        ),
    ]
