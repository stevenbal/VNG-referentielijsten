# Generated by Django 2.1.4 on 2019-02-08 13:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('selectielijst', '0002_auto_20190208_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultaat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='uuid')),
                ('nummer', models.PositiveSmallIntegerField(help_text='Nummer van het resultaat. Dit wordt samengesteld met het procestype en generiek resultaat indien van toepassing.', unique=True, verbose_name='nummer')),
                ('naam', models.CharField(help_text='Benaming van het procestype', max_length=40, verbose_name='procestypenaam')),
                ('omschrijving', models.CharField(blank=True, help_text='Omschrijving van het specifieke resultaat', max_length=100, verbose_name='omschrijving')),
                ('herkomst', models.CharField(help_text="Voorbeeld: 'Risicoanalyse', 'Systeemanalyse' of verwijzing naar Wet- en regelgeving", max_length=100, verbose_name='herkomst')),
                ('waardering', models.CharField(choices=[('bewaren', 'Bewaren'), ('vernietigen', 'Vernietigen')], max_length=20, verbose_name='waardering')),
                ('procestermijn', models.CharField(blank=True, choices=[('nihil', 'Nihil'), ('bestaansduur_procesobject', 'De bestaans- of geldigheidsduur van het procesobject.'), ('ingeschatte_bestaansduur_procesobject', 'De ingeschatte maximale bestaans- of geldigheidsduur van het procesobject.'), ('vast_te_leggen_datum', 'Een tijdens het proces vast te leggen datum waarop de geldigheid van het procesobject komt te vervallen. '), ('samengevoegd_met_bewaartermijn', 'De procestermijn is samengevoegd met de bewaartermijn.')], max_length=50, verbose_name='procestermijn')),
                ('bewaartermijn', models.DurationField(blank=True, null=True, verbose_name='bewaartermijn')),
                ('toelichting', models.TextField(blank=True, verbose_name='toelichting')),
                ('algemeen_bestuur_en_inrichting_organisatie', models.BooleanField(default=False, verbose_name='algemeen bestuur en inrichting organisatie')),
                ('bedrijfsvoering_en_personeel', models.BooleanField(default=False, verbose_name='bedrijfsvoering en personeel')),
                ('publieke_informatie_en_registratie', models.BooleanField(default=False, verbose_name='publieke informatie en registratie')),
                ('burgerzaken', models.BooleanField(default=False, verbose_name='burgerzaken')),
                ('veiligheid', models.BooleanField(default=False, verbose_name='veiligheid')),
                ('verkeer_en_vervoer', models.BooleanField(default=False, verbose_name='verkeer en vervoer')),
                ('economie', models.BooleanField(default=False, verbose_name='economie')),
                ('onderwijs', models.BooleanField(default=False, verbose_name='onderwijs')),
                ('sport_cultuur_en_recreatie', models.BooleanField(default=False, verbose_name='sport, cultuur en recreatie')),
                ('sociaal_domein', models.BooleanField(default=False, verbose_name='sociaal domein')),
                ('volksgezonheid_en_milieu', models.BooleanField(default=False, verbose_name='volksgezonheid en milieu')),
                ('vhrosv', models.BooleanField(default=False, verbose_name='VHROSV')),
                ('heffen_belastingen', models.BooleanField(default=False, verbose_name='heffen belastingen etc.')),
                ('alle_taakgebieden', models.BooleanField(default=False, verbose_name='alle taakgebieden')),
                ('generiek_resultaat', models.ForeignKey(blank=True, help_text='Voor specifieke resultaten, geef aan bij welk generiek resultaat deze hoort', limit_choices_to={'generiek_resultaat__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='selectielijst.Resultaat', verbose_name='generiek resultaat')),
                ('proces_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selectielijst.ProcesType', verbose_name='procestype')),
            ],
            options={
                'verbose_name': 'resultaat',
                'verbose_name_plural': 'resultaten',
            },
        ),
        migrations.AlterUniqueTogether(
            name='resultaat',
            unique_together={('proces_type', 'generiek_resultaat', 'nummer')},
        ),
    ]
