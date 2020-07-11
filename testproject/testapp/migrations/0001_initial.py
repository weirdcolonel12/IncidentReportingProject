# Generated by Django 3.0.3 on 2020-07-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subincidenttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='ReportingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('corporate headoffice', 'Corporate Headoffice'), ('main area', 'Main Area'), ('far away', 'Far Away')], max_length=64)),
                ('incidentdescription', models.TextField()),
                ('date', models.DateTimeField()),
                ('incidentlocation', models.TextField(blank=True, default='')),
                ('internalseverity', models.CharField(choices=[('severe', 'Severe'), ('moderate', 'Moderate'), ('minor', 'Minor')], max_length=64)),
                ('suspectedcause', models.TextField(blank=True, default='')),
                ('immediateactionstaken', models.TextField(blank=True, default='')),
                ('reportedby', models.CharField(max_length=264)),
                ('subincidenttypes', models.ManyToManyField(blank=True, null=True, to='testapp.Subincidenttype', verbose_name='subincident types')),
            ],
        ),
    ]
