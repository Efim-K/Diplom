from rest_framework.serializers import ModelSerializer, SerializerMethodField

from course.models import Answers, Course, Questions
from users.permissions import IsTeacher


class CourseSerializer(ModelSerializer):
    """Serializer для курса"""

    class Meta:
        model = Course
        fields = "__all__"


class QuestionsSerializer(ModelSerializer):
    """Serializer для вопроса"""

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
