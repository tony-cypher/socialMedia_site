# Generated by Django 4.1 on 2024-01-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0004_alter_comment_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="posted_by",
            field=models.CharField(default="cypher", max_length=100),
            preserve_default=False,
        ),
    ]
