from rest_framework.serializers import ValidationError

class AnswerStudentValidators:

    def __call__(self, value):
        """Проверка валидности полей ответа студентов"""

        val = dict(value)

        # Проверка зависимости ответа к вопросу
        if val.get("answer").question != val.get("question"):
            raise ValidationError("Ответ должен быть к заданному вопросу")
