# Generated by Django 4.2.7 on 2023-11-04 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('removed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eng_word', models.CharField(max_length=30)),
                ('pl_word', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcards.category')),
            ],
            options={
                'verbose_name_plural': 'flashcards',
            },
        ),
    ]
