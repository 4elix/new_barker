# Generated by Django 5.0.7 on 2024-08-05 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='twitter',
            new_name='twitter_x',
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/product/'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='image',
            field=models.ImageField(upload_to='image/team/', verbose_name='Фото работника'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='position',
            field=models.CharField(choices=[('с', 'Стажер'), ('к', 'Кондитер'), ('п', 'Пекарь'), ('гп', 'Главный пекарь')], default='c', max_length=2, verbose_name='Должность'),
        ),
    ]