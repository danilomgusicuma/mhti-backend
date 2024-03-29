# Generated by Django 4.0.4 on 2022-08-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhti', '0005_rename_hasfamiliarhistory_employeeanswer_hasfamilyhistory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeanswer',
            old_name='hasHealthcareCoverage',
            new_name='hasReceivedTreatment',
        ),
        migrations.RemoveField(
            model_name='employeeanswer',
            name='birthDate',
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='betterOfDead',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='cantStopWorrying',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='downDepressedHopeless',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='easilyAnnoyed',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='feelingAfraid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='feelingBad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='interestOrPleasure',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='medicalLeave',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='nervousAnxious',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='openToDiscussWorkspace',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='poorAppetiteOvereating',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='race',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='slowOrFast',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='talkToCoworker',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='talkToSupervisor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='tiredLittleEnergy',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='troubleConcentrating',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='troubleFallingAsleep',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='troubleRelaxing',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='worryingToMuch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employeeanswer',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
