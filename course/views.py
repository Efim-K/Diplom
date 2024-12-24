from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from course.models import Answers, Course, Questions
from course.serializers import (AnswersSerializer, CourseSerializer,
                                QuestionsSerializer)


class CourseCreateAPIView(CreateAPIView):
    """Создание курса"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListAPIView(ListAPIView):
    """Список всех курсов"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveAPIView(RetrieveAPIView):
    """Получение информации о конкретном курсе"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateAPIView(UpdateAPIView):
    """Изменение информации о конкретном курсе"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDestroyAPIView(DestroyAPIView):
    """Удаление конкретного курса"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class QuestionsCreateAPIView(CreateAPIView):
    """Создание вопроса теста по курсу"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionsListAPIView(ListAPIView):
    """Список всех вопросов теста по конкретному курсу"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionsUpdateAPIView(UpdateAPIView):
    """Изменение информации о конкретном вопросе теста"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionsDestroyAPIView(DestroyAPIView):
    """Удаление конкретного вопроса теста"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class AnswersCreateAPIView(CreateAPIView):
    """Создание ответа к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class AnswersListAPIView(ListAPIView):
    """Список всех ответов к вопросу теста по конкретному вопросу"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class AnswersUpdateAPIView(UpdateAPIView):
    """Изменение информации о конкретном ответе к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class AnswersDestroyAPIView(DestroyAPIView):
    """Удаление конкретного ответа к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
