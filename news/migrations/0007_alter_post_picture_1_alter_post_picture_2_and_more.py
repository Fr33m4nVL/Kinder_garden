# Generated by Django 4.1.2 on 2022-10-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_rename_pictures_post_picture_1_post_picture_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture_1',
            field=models.ImageField(blank=True, null=True, upload_to='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture_2',
            field=models.ImageField(blank=True, null=True, upload_to='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture_3',
            field=models.ImageField(blank=True, null=True, upload_to='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture_4',
            field=models.ImageField(blank=True, null=True, upload_to='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture_5',
            field=models.ImageField(blank=True, null=True, upload_to='content'),
        ),
    ]
