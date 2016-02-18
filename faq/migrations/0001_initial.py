# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(help_text='The actual question itself.', verbose_name='question')),
                ('answer', models.TextField(help_text='The answer text.', verbose_name='answer', blank=True)),
                ('protected', models.BooleanField(default=False, help_text='Set true if this question is only visible by authenticated users.', verbose_name='is protected')),
                ('sort_order', models.IntegerField(default=0, help_text='The order you would like the question to be displayed.', verbose_name='sort order')),
            ],
            options={
                'ordering': ['sort_order'],
                'verbose_name': 'Frequent asked question',
                'verbose_name_plural': 'Frequently asked questions',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('sort_order', models.IntegerField(default=0, help_text='The order you would like the topic to be displayed.', verbose_name='sort order')),
            ],
            options={
                'ordering': ['sort_order', 'name'],
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(related_name='questions', verbose_name='topic', to='faq.Topic'),
        ),
    ]
