from rest_framework.serializers import ValidationError

from course.models import AnswerStudent


class AnswerStudentValidators:

    def __call__(self, value):
        """Проверка валидности полей ответа студентов"""

        val = dict(value)

        # Проверка уникальности ответа студента на вопрос
        if AnswerStudent.objects.filter(
            owner=val.get("owner"), question=val.get("question")
        ).exists():
            raise ValidationError("Уже имеется ответ на вопрос")

        # Проверка зависимости ответа к вопросу
        if val.get("answer").question != val.get("question"):
            raise ValidationError("Ответ должен быть к заданному вопросу")



