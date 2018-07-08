# Generated by Django 2.2.dev20180610131139 on 2018-07-08 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_text', models.CharField(max_length=5000)),
                ('pub_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_text', models.CharField(max_length=5000)),
                ('pub_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='SampleText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_text', models.CharField(max_length=5000)),
                ('pub_date', models.DateTimeField(verbose_name='date created')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.Query')),
            ],
        ),
        migrations.AddField(
            model_name='generatedtext',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.Query'),
        ),
    ]
