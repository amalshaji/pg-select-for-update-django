# Generated by Django 5.0.1 on 2024-02-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_processed_at', models.DateTimeField(db_index=True, null=True)),
            ],
        ),
    ]
