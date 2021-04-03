# Generated by Django 3.1.5 on 2021-02-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayosha', '0002_auto_20210226_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_img_name', models.CharField(max_length=20, null=True)),
                ('office_img', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ResidencialImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_img_name', models.CharField(max_length=20, null=True)),
                ('res_img', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageShow',
        ),
        migrations.DeleteModel(
            name='projects',
        ),
    ]