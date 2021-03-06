# Generated by Django 3.1.5 on 2021-01-20 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.CharField(blank=True, max_length=2000)),
                ('skills', models.CharField(blank=True, max_length=2000)),
                ('aoi', models.CharField(blank=True, max_length=2000)),
                ('github', models.CharField(blank=True, max_length=200)),
                ('linkedin', models.CharField(blank=True, max_length=200)),
                ('divisions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.section')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ut1', models.CharField(blank=True, max_length=200)),
                ('ut2', models.CharField(blank=True, max_length=200)),
                ('ut3', models.CharField(blank=True, max_length=200)),
                ('ut1p', models.ImageField(blank=True, upload_to='plots')),
                ('ut2p', models.ImageField(blank=True, upload_to='plots')),
                ('ut3p', models.ImageField(blank=True, upload_to='plots')),
                ('ut1pb', models.ImageField(blank=True, upload_to='plots')),
                ('ut2pb', models.ImageField(blank=True, upload_to='plots')),
                ('ut3pb', models.ImageField(blank=True, upload_to='plots')),
                ('ut12', models.ImageField(blank=True, upload_to='plots')),
                ('ut13', models.ImageField(blank=True, upload_to='plots')),
                ('ut23', models.ImageField(blank=True, upload_to='plots')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_field', models.CharField(blank=True, max_length=2000, null=True)),
                ('divisions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.section')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_field', models.CharField(blank=True, max_length=2000, null=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
