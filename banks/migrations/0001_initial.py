# Generated by Django 2.2.1 on 2019-05-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]