# Generated by Django 2.2 on 2021-09-25 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopify_variant_id', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('taxable', models.BooleanField(null=True)),
                ('requires_shipping', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopify_listing_id', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('vendor', models.CharField(blank=True, max_length=100, null=True)),
                ('product_type', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('published_at', models.DateTimeField(null=True)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shopify.Variant')),
            ],
        ),
    ]
