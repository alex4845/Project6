# Generated by Django 4.1 on 2022-09-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shtors', '0008_remove_list1_img_remove_list2_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('date_go', models.CharField(max_length=25)),
            ],
        ),
    ]
