from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAdminUser

from course.models import Answers, AnswerStudent, Course, Questions
from course.serializers import (AnswersSerializer, AnswerStudentSerializer, CourseSerializer,
                                QuestionsSerializer)
from users.permissions import IsOwner, IsTeacher


class CourseCreateApiView(CreateAPIView):
    """Создание курса"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsTeacher | IsAdminUser,)

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
    serializer_class = CourseSerializer


class CourseUpdateApiView(UpdateAPIView):
    """Изменение информации о конкретном курсе"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (
        IsTeacher | IsAdminUser,
        IsOwner | IsAdminUser,
    )


class CourseDestroyApiView(DestroyAPIView):
    """Удаление конкретного курса"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (
        IsTeacher | IsAdminUser,
        IsOwner | IsAdminUser,
    )


class QuestionsCreateApiView(CreateAPIView):
    """Создание вопроса по курсу"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = (IsTeacher | IsAdminUser,)

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
    permission_classes = (
        IsTeacher | IsAdminUser,
        IsOwner | IsAdminUser,
    )


class QuestionsDestroyApiView(DestroyAPIView):
    """Удаление конкретного вопроса теста"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = (
        IsTeacher | IsAdminUser,
        IsOwner | IsAdminUser,
    )


class AnswersCreateApiView(CreateAPIView):
    """Создание ответа к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = (IsTeacher | IsAdminUser,)

    def perform_create(self, serializer):
        """Определение владельца ответа"""

        answers = serializer.save()
        answers.owner = self.request.user
        answers.save()


class AnswersListApiView(ListAPIView):
    """Список всех ответов к вопросу теста по конкретному вопросу"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class AnswersUpdateApiView(UpdateAPIView):
    """Изменение информации о конкретном ответе к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = (
        IsTeacher | IsAdminUser,
        IsOwner | IsAdminUser,
    )


class AnswersDestroyApiView(DestroyAPIView):
    """Удаление конкретного ответа к вопросу теста"""

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = (
        IsTeacher | IsAdminUser,
        IsOwner | IsAdminUser,
    )


class AnswerStudentCreateApiView(CreateAPIView):
    """Создание ответа студента на вопрос теста"""

    queryset = AnswerStudent.objects.all()
    serializer_class = AnswerStudentSerializer

    def perform_create(self, serializer):
        """Определение владельца ответа студента"""

        answer_student = serializer.save()
        # сохраняем текущего владельца
        answer_student.owner = self.request.user

        if answer_student.answer.correct:
            answer_student.is_correct = True

        # увеличиваем счетчик правильных ответов с фильтром по пользователю и курсу
        answer_student.count_of_correct = AnswerStudent.objects.filter(owner=self.request.user,
                                                                             answer__question__course=answer_student.answer.question.course,
                                                                             is_correct=True).count()
        # увеличиваем счетчик заданных вопросов пользователю и курсу
        answer_student.count_of_question = AnswerStudent.objects.filter(owner=self.request.user,
                                                                             answer__question__course=answer_student.answer.question.course).count()

        answer_student.save()

    def get_queryset(self):
        """Ограничение доступа к ответам студента по текущему владельцу"""

        return AnswerStudent.objects.filter(owner=self.request.user)


class AnswerStudentListApiView(ListAPIView):
    """Список всех ответов студента на вопросы теста"""

    queryset = AnswerStudent.objects.all()
    serializer_class = AnswerStudentSerializer


class AnswerStudentDestroyApiView(DestroyAPIView):
    """Удаление ответов студента"""

    queryset = Answers.objects.all()
    serializer_class = AnswerStudentSerializer
    permission_classes = (
        IsTeacher | IsAdminUser,
        IsOwner | IsAdminUser,
    )


class AnswerStudentRetrieveApiView(RetrieveAPIView):
    """Получение информации об ответе студента"""

    queryset = AnswerStudent.objects.all()
    serializer_class = AnswerStudentSerializer
