# Generated by Django 3.2.4 on 2021-06-24 09:59

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ann_title', models.CharField(max_length=255, verbose_name='Announcement title')),
                ('ann_body', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Announcement')),
                ('ann_time_in', models.DateTimeField(auto_now_add=True, verbose_name='Time of announcement creation')),
                ('ann_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author of announcement')),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_body', models.TextField(verbose_name='Comment')),
                ('com_time_in', models.DateTimeField(auto_now_add=True, verbose_name='Time of comment creation')),
                ('com_confirmed', models.BooleanField(default=False, verbose_name='Comment confirmed by announcement author')),
                ('com_ann', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='announcements.announcement', verbose_name='Commented announcement')),
                ('com_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author of comment')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.AddField(
            model_name='announcement',
            name='ann_category',
            field=models.ManyToManyField(to='announcements.Category', verbose_name='Category of announcement'),
        ),
    ]