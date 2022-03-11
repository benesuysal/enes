# Generated by Django 4.0.3 on 2022-03-10 14:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.CharField(max_length=12, verbose_name='Doğum Tarihi'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50, verbose_name='İsim Soyisim'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nat_id',
            field=models.CharField(max_length=11, verbose_name='TC No'),
        ),
        migrations.AlterField(
            model_name='person',
            name='seri_no',
            field=models.CharField(max_length=20, verbose_name='Seri Numara'),
        ),
    ]
