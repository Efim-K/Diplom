# Generated by Django 5.1.4 on 2024-12-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answer", models.CharField(max_length=255, verbose_name="Ответ")),
                (
                    "correct",
                    models.BooleanField(default=False, verbose_name="Правильный ответ"),
                ),
            ],
            options={
                "verbose_name": "Ответ",
                "verbose_name_plural": "Ответы",
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Название курса"),
                ),
                (
                    "description",
                    models.TextField(
                        blank="True", null="True", verbose_name="Описание курса"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank="True",
                        null="True",
                        upload_to="courses/",
                        verbose_name="Изображение курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Questions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=255, verbose_name="Вопрос")),
            ],
            options={
                "verbose_name": "Вопрос",
                "verbose_name_plural": "Вопросы",
            },
        ),
    ]
