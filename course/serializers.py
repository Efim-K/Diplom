from rest_framework.serializers import ModelSerializer

from course.models import Answers, Course, Questions


class CourseSerializer(ModelSerializer):
    """
    Serializer для курса
    """

    class Meta:
        model = Course
        fields = "__all__"


class QuestionsSerializer(ModelSerializer):
    """
    Serializer для вопроса
    """

    class Meta:
        model = Questions
        fields = "__all__"


class AnswersSerializer(ModelSerializer):
    """
    Serializer для ответа
    """

    class Meta:
        model = Answers
        fields = ["answer"]
