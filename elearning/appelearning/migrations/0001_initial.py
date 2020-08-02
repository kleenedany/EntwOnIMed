# Generated by Django 3.0.6 on 2020-08-01 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('test_description', models.CharField(max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appelearning.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appelearning.MultipleChoiceTest')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('is_answer_right', models.CharField(choices=[('Richtig', 'Right'), ('Falsch', 'False')], default='Falsch', max_length=10)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appelearning.MultipleChoiceQuestion')),
            ],
        ),
    ]
