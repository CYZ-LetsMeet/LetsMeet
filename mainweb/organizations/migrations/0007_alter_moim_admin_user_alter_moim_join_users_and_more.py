# Generated by Django 4.1 on 2022-08-24 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("organizations", "0006_alter_moim_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moim",
            name="admin_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="moim_admin_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="moim",
            name="join_users",
            field=models.ManyToManyField(
                blank=True, related_name="moim_users", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="moim",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True, editable=False, null=True, populate_from="name"
            ),
        ),
    ]