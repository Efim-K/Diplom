from rest_framework.serializers import ValidationError

from course.models import AnswerStudent


class AnswerStudentValidators:

    def __call__(self, value):
        """Проверка валидности полей ответа студентов"""

        # Проверка уникальности ответа студента на вопрос
        if AnswerStudent.objects.filter(
            owner=val.get("owner"), question=val.get("question")
        ).exists():
            raise ValidationError("Уже имеется ответ на вопрос")
