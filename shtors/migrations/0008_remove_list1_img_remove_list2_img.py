# Generated by Django 4.1 on 2022-08-18 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shtors', '0007_rename_img_list3_img3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list1',
            name='img',
        ),
        migrations.RemoveField(
            model_name='list2',
            name='img',
        ),
    ]
