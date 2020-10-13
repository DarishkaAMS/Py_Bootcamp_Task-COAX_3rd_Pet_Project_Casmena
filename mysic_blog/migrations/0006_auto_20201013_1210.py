# Generated by Django 3.1 on 2020-10-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysic_blog', '0005_auto_20201012_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='In Progress', max_length=255),
        ),
    ]
