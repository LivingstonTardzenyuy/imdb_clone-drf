# Generated by Django 4.2.7 on 2023-11-25 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_watchlist_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist_app.streamplatform'),
        ),
    ]
