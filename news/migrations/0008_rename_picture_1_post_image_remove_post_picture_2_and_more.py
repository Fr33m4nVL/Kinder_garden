# Generated by Django 4.1.2 on 2022-10-27 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_post_picture_1_alter_post_picture_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='picture_1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='picture_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='picture_3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='picture_4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='picture_5',
        ),
    ]
