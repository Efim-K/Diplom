from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from course.models import Answers, Course, Questions
from course.serializers import (AnswersSerializer, CourseRetrieveSerializer,
                                CourseSerializer, QuestionsSerializer)


class CourseCreateApiView(CreateAPIView):
    """Создание курса"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListApiView(ListAPIView):
    """Список всех курсов"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveApiView(RetrieveAPIView):
    """Получение информации о конкретном курсе"""

    queryset = Course.objects.all()
    serializer_class = CourseRetrieveSerializer


class CourseUpdateApiView(UpdateAPIView):
    """Изменение информации о конкретном курсе"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDestroyApiView(DestroyAPIView):
    """Удаление конкретного курса"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class QuestionsCreateApiView(CreateAPIView):
    """Создание вопроса теста по курсу"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionsListApiView(ListAPIView):
    """Список всех вопросов теста по конкретному курсу"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionsUpdateApiView(UpdateAPIView):
    """Изменение информации о конкретном вопросе теста"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionsDestroyApiView(DestroyAPIView):
    """Удаление конкретного вопроса теста"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class AnswersCreateApiView(CreateAPIView):
    """Создание ответа к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class AnswersListApiView(ListAPIView):
    """Список всех ответов к вопросу теста по конкретному вопросу"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class AnswersUpdateApiView(UpdateAPIView):
    """Изменение информации о конкретном ответе к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class AnswersDestroyApiView(DestroyAPIView):
    """Удаление конкретного ответа к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
