# Generated by Django 4.1.2 on 2022-10-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('relationship', models.CharField(choices=[('Immediate', 'Immediate'), ('Distant', 'Distant'), ('Friend', 'Friend')], max_length=50)),
            ],
        ),
    ]