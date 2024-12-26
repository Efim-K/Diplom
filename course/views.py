from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAdminUser
from course.models import Answers, Course, Questions
from course.serializers import (AnswersSerializer, CourseRetrieveSerializer,
                                CourseSerializer, QuestionsSerializer)
from users.permissions import IsTeacher, IsOwner


class CourseCreateApiView(CreateAPIView):
    """Создание курса"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsTeacher,)

    def perform_create(self, serializer):
        """Определение владельца курса"""

        course = serializer.save()
        course.owner = self.request.user
        course.save()


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
    permission_classes = (IsTeacher, IsOwner | IsAdminUser,)


class CourseDestroyApiView(DestroyAPIView):
    """Удаление конкретного курса"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsTeacher, IsOwner | IsAdminUser,)


class QuestionsCreateApiView(CreateAPIView):
    """Создание вопроса по курсу"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = (IsTeacher, )

    def perform_create(self, serializer):
        """Определение владельца вопроса"""

        questions = serializer.save()
        questions.owner = self.request.user
        questions.save()


class QuestionsListApiView(ListAPIView):
    """Список всех вопросов теста по конкретному курсу"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionsUpdateApiView(UpdateAPIView):
    """Изменение информации о конкретном вопросе теста"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = (IsTeacher, IsOwner | IsAdminUser,)


class QuestionsDestroyApiView(DestroyAPIView):
    """Удаление конкретного вопроса теста"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = (IsTeacher, IsOwner | IsAdminUser,)


class AnswersCreateApiView(CreateAPIView):
    """Создание ответа к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = (IsTeacher,)


class AnswersListApiView(ListAPIView):
    """Список всех ответов к вопросу теста по конкретному вопросу"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class AnswersUpdateApiView(UpdateAPIView):
    """Изменение информации о конкретном ответе к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = (IsTeacher, IsOwner | IsAdminUser,)


class AnswersDestroyApiView(DestroyAPIView):
    """Удаление конкретного ответа к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = (IsTeacher, IsOwner | IsAdminUser,)


