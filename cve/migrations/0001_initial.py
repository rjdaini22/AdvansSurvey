# Generated by Django 4.0.5 on 2022-06-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CVE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve_name', models.CharField(max_length=20)),
                ('cve_summary', models.TextField(default='...')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('cve_criticity', models.CharField(choices=[(0, 'Faible'), (1, 'Moyen'), (2, 'Urgent')], max_length=1)),
                ('cve_status', models.CharField(choices=[(0, 'Nouveau'), (1, 'Archivé')], max_length=1)),
            ],
        ),
    ]
