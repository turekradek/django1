# Generated by Django 4.0 on 2021-12-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0002_zawodnik_belki_zawodnik_email_zawodnik_pas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zawodnik',
            name='fotka',
            field=models.ImageField(blank=True, null=True, upload_to='fotki'),
        ),
        migrations.AddField(
            model_name='zawodnik',
            name='poczatek',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zawodnik',
            name='belki',
            field=models.PositiveSmallIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default=0),
        ),
        migrations.AlterField(
            model_name='zawodnik',
            name='pas',
            field=models.CharField(choices=[('BIAŁY', 'BIAŁY'), ('NIEBIESKI', 'NIEBIESKI'), ('PURPURA', 'PURPURA'), ('BRĄZOWY', 'BRĄZOWY'), ('CZARNY', 'CZARNY')], default='BIAŁY', max_length=20),
        ),
    ]
