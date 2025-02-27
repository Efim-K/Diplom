# Generated by Django 5.1.4 on 2024-12-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0006_rename_students_answerstudent"),
    ]

    operations = [
        migrations.AddField(
            model_name="answerstudent",
            name="count_of_correct",
            field=models.IntegerField(
                default=0, verbose_name="Количество правильных ответов"
            ),
        ),
        migrations.AddField(
            model_name="answerstudent",
            name="count_of_question",
            field=models.IntegerField(
                default=0, verbose_name="Количество вопросов курса"
            ),
        ),
    ]
