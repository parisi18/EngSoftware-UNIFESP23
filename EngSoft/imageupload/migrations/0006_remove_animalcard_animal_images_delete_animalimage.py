# Generated by Django 4.2.4 on 2023-12-06 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0005_alter_animalimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalcard',
            name='animal_images',
        ),
        migrations.DeleteModel(
            name='AnimalImage',
        ),
    ]
