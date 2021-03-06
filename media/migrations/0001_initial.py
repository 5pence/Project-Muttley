# Generated by Django 2.2.3 on 2019-08-04 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='')),
                ('type', models.CharField(choices=[['image', 'Image'], ['video', 'Video']], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
        ),
    ]
