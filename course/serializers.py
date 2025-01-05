from rest_framework.serializers import (ModelSerializer, ReadOnlyField,
                                        SerializerMethodField)

from course.models import Answers, AnswerStudent, Course, Questions
from course.validators import AnswerStudentValidators

from rest_framework.serializers import ValidationError

class QuestionsSerializer(ModelSerializer):
    """Serializer для вопроса"""

    answers = SerializerMethodField()

    def get_answers(self, instance):
        """Возвращает список id ответов в вопросе теста"""
        return [
            {"id": obj.id, "answer": obj.answer}
            for obj in Answers.objects.filter(question=instance)
        ]

    class Meta:
        model = Questions
        exclude = [
            "owner",
        ]
        ordering = ["question", "answer"]


class AnswersSerializer(ModelSerializer):
    """Serializer для ответа"""

    class Meta:
        model = Answers
        fields = "__all__"


class AnswerStudentSerializer(ModelSerializer):
    """Serializer для ответа"""

    info_course = SerializerMethodField()

    def get_info_course(self, instance):
        """Возвращает информацию о курсах"""

        if instance.count_of_question != 0:
            percent_correct = (
                instance.count_of_correct * 100 / instance.count_of_question
            )
            result = {
                "тема id": instance.answer.question.course.id,
                "Название темы": instance.answer.question.course.name,
                "Вопрос id": instance.answer.question.id,
                "Вопрос": instance.answer.question.question,
                "Выдан ответ": instance.answer.answer,
                "Кол-во отвеченных вопросов": instance.count_of_question,
                "Кол-во правильных ответов": instance.count_of_correct,
                "Процент правильных ответов": int(percent_correct),
            }
            return result
        else:
            result = {
                "id": instance.answer.question.course.id,
                "Название темы": instance.answer.question.course.name,
                "Кол-во отвеченных вопросов": instance.count_of_question,
            }
            return result

    def validate(self, data):
        """Проверяет корректность ответа"""
        request = self.context.get('request')
        # Получаем текущего пользователя
        user = request.user

        # Если ответ есть и он принадлежит текущему пользователю,
        if AnswerStudent.objects.filter(owner=user, question=data.get("question")).exists():
            raise ValidationError("Уже имеется ответ на вопрос")

        return data


    class Meta:
        model = AnswerStudent
        fields = "__all__"
        # read_only_fields = ["owner",]
        validators = [AnswerStudentValidators()]


class CourseSerializer(ModelSerializer):
    """Serializer для вопросов курса"""

    count_of_questions = SerializerMethodField()
    questions = SerializerMethodField()
    answer_student = SerializerMethodField()

    def get_questions(self, course):
        """Возвращает список вопросов курса"""

        return [
            {"id": obj.id, "question": obj.question}
            for obj in Questions.objects.filter(course=course)
        ]

    def get_count_of_questions(self, course):
        """Возвращает количество вопросов в курсе"""

        return Questions.objects.filter(course=course).count()

    def get_answer_student(self, instance):
        """Возвращает список студентов курса"""

        # Получаем текущего пользователя
        user = self.context["request"].user

        # Получаем все AnswerStudent, связанные с текущим курсом
        try:
            answer_student = AnswerStudent.objects.filter(
                owner=user, question__course=instance
            ).latest("id")

            count_question = answer_student.count_of_question
            count_correct = answer_student.count_of_correct
            percent_correct = 0
            if count_question != 0:
                percent_correct = count_correct * 100 / count_question
            return {
                "Кол-во отвеченных вопросов": count_question,
                "Кол-во правильных ответов": count_correct,
                "Процент правильных ответов": int(percent_correct),
            }
        except AnswerStudent.DoesNotExist:
            return {
                "Кол-во отвеченных вопросов": 0,
                "Кол-во правильных ответов": 0,
                "Процент правильных ответов": 0,
            }

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
            "count_of_questions",
            "questions",
            "answer_student",
            "owner",
        ]
