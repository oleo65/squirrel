# Generated by Django 3.1.4 on 2020-12-25 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stash', '0003_inventoryitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='StashSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='stash.product')),
                ('product_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='stash.productgroup')),
                ('stash_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stash.stashlocation')),
            ],
        ),
    ]
