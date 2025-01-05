from django.db import models

from config import settings

NULLABLE = {"blank": "True", "null": "True"}


class Course(models.Model):
    """Модель курса"""

    name = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса", **NULLABLE)
    image = models.ImageField(
        upload_to="courses/", verbose_name="Изображение курса", **NULLABLE
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Создатель курса",
        **NULLABLE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Questions(models.Model):
    """Вопросы теста по курсу"""

    question = models.CharField(max_length=255, verbose_name="Вопрос")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Создатель вопроса теста",
        **NULLABLE,
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answers(models.Model):
    """Ответы на вопросы теста"""

    question = models.ForeignKey(
        Questions, on_delete=models.CASCADE, verbose_name="Вопрос"
    )
    answer = models.CharField(max_length=255, verbose_name="Ответ")
    correct = models.BooleanField(default=False, verbose_name="Правильный ответ")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Создатель ответа на вопрос",
        **NULLABLE,
    )

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class AnswerStudent(models.Model):
    """Ответы на вопросы по курсу от студентов"""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        **NULLABLE,
    )
    question = models.ForeignKey(
        Questions,
        on_delete=models.CASCADE,
        verbose_name="Вопрос",
    )
    answer = models.ForeignKey(
        Answers,
        on_delete=models.CASCADE,
        verbose_name="Ответ",
        **NULLABLE,
    )
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")
    count_of_question = models.IntegerField(
        default=0, verbose_name="Количество вопросов курса"
    )
    count_of_correct = models.IntegerField(
        default=0, verbose_name="Количество правильных ответов"
    )

    def __str__(self):
        return f"{self.owner} - {self.question} - {self.answer}"

    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователей"
