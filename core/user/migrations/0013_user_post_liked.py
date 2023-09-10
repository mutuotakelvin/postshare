# Generated by Django 4.0 on 2023-09-10 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
        ('core_user', '0012_rename_avator_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='post_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_post.Post'),
        ),
    ]
