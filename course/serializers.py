from rest_framework.serializers import ModelSerializer, SerializerMethodField

from course.models import Answers, AnswerStudent, Course, Questions
from course.validators import AnswerStudentValidators


class CourseSerializer(ModelSerializer):
    """Serializer для курса"""

    class Meta:
        model = Course
        fields = "__all__"


class QuestionsSerializer(ModelSerializer):
    """Serializer для вопроса"""

    answers = SerializerMethodField()

    def get_answers(self, instance):
        """Возвращает список id ответов в вопросе теста"""
        return [obj.id for obj in Answers.objects.filter(question=instance)]

    class Meta:
        model = Questions
        fields = "__all__"


class AnswersSerializer(ModelSerializer):
    """Serializer для ответа"""

    class Meta:
        model = Answers
        fields = "__all__"


class CourseRetrieveSerializer(ModelSerializer):
    """Serializer для детального просмотра вопросов курса"""

    questions = SerializerMethodField()
    count_of_questions = SerializerMethodField()

    def get_questions(self, course):
        """Возвращает список вопросов курса"""

        return [obj.question for obj in Questions.objects.filter(course=course)]

    def get_count_of_questions(self, course):
        """Возвращает количество вопросов в курсе"""

        return Questions.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = "__all__"


class AnswerStudentSerializer(ModelSerializer):
    """Serializer для ответа"""

    course = SerializerMethodField()
    count_of_questions = SerializerMethodField()
    result = SerializerMethodField()

    def get_course(self, instance):
        """Возвращает курс, к которому относится ответ"""

        return (
            instance.answer.question.course.name if instance.answer.question else None
        )

    def get_count_of_questions(self, instance):
        """Возвращает количество отвеченных вопросов по курсу"""

        return AnswerStudent.objects.filter(
            owner=instance.owner,
            answer__question__course=instance.answer.question.course,
        ).count()

    def get_result(self, instance):
        """Возвращает количество правильно отвеченных вопросов по курсу"""

        return AnswerStudent.objects.filter(
            owner=instance.owner,
            answer__question__course=instance.answer.question.course,
            is_correct=True,
        ).count()

    class Meta:
        model = AnswerStudent
        fields = "__all__"
        validators = [AnswerStudentValidators()]
