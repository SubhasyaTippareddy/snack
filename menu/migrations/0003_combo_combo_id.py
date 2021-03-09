# Generated by Django 3.1.3 on 2021-03-09 16:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20210309_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='combo_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]