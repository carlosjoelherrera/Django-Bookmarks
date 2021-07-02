# Generated by Django 3.2.5 on 2021-07-02 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('url', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('Bookmark', 'Bookmark'), ('Folder', 'Folder')], default='Bookmark', max_length=100)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.bookmark')),
                ('tags', models.ManyToManyField(to='core.Tag')),
            ],
        ),
    ]
