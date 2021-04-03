# Generated by Django 3.1.7 on 2021-04-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayosha', '0003_auto_20210226_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('desc', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='cname',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='officeimage',
            name='office_img_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='residencialimage',
            name='res_img_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='designation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='member_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
