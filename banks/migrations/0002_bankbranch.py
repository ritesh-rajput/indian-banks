# Generated by Django 2.2.1 on 2019-05-04 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(db_index=True, max_length=11, unique=True)),
                ('branch_name', models.CharField(db_index=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(db_index=True, max_length=50)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.Bank')),
            ],
            options={
                'unique_together': {('bank', 'branch_name', 'city')},
            },
        ),
    ]