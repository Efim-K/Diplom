# Generated by Django 5.1.4 on 2024-12-24 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("course", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="owner",
            field=models.ForeignKey(
                blank="True",
                null="True",
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель курса",
            ),
        ),
        migrations.AddField(
            model_name="questions",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="course.course",
                verbose_name="Курс",
            ),
        ),
        migrations.AddField(
            model_name="answers",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="course.questions",
                verbose_name="Вопрос",
            ),
        ),
    ]