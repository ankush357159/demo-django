# Generated by Django 2.2.12 on 2022-05-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
            ],
        ),
    ]