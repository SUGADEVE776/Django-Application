# Generated by Django 4.2.2 on 2023-07-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('touch_screen', models.BooleanField()),
            ],
            options={
                'db_table': 'Laptop',
                'ordering': ('price',),
            },
        ),
    ]
