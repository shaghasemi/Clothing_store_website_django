# Generated by Django 5.0.1 on 2024-03-31 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productsModule', '0005_remove_weakpointscomment_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentsmodel',
            old_name='text',
            new_name='commentText',
        ),
    ]
