# Generated by Django 5.0.4 on 2024-05-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_category_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]
