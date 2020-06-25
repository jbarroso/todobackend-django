# Generated by Django 3.0.7 on 2020-06-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('completed', models.BooleanField(default=False)),
                ('order', models.IntegerField(db_column='position', default=0)),
            ],
        ),
    ]
