# Generated by Django 2.2.6 on 2020-03-04 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200304_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Publisher'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='title',
            field=models.TextField(max_length=12, null=True),
        ),
    ]