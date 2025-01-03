from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course, Questions, Answers, AnswerStudent
from users.models import User


class CourseTestCase(APITestCase):
    """Тестирование API для курсов"""

    def setUp(self):
        """Создание пользователя и курса с вопросом и ответом"""
        self.user = User.objects.create(email="123@123.123")
        self.user.is_staff = True
        self.course = Course.objects.create(
            owner=self.user,
            name="алгебра",
            description="Отдел математики, изучающий свойства величин",

        )
        self.questions = Questions.objects.create(
            course=self.course,
            question="Что такое квадрат?",
            owner=self.user,
        )
        self.answers = Answers.objects.create(
            question=self.questions,
            owner=self.user,
            answer="Число, умноженное на само себя",
            correct=True,
        )
        self.answer_student = AnswerStudent.objects.create(
            answer=self.answers,
            question=self.questions,
            owner=self.user,
            # is_correct=False,
        )

        self.client.force_authenticate(user=self.user)

    def test_course_create(self):
        """проверка создания нового курса"""
        url = reverse("course:course-create")
        data = {"name": "физика", "description": "Отдел физики"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)

    def test_course_list(self):
        """проверка получения списка всех курсов"""
        url = reverse("course:course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "алгебра")

    def test_course_retrieve(self):
        """проверка получения конкретного курса"""
        url = reverse("course:course-retrieve", kwargs={"pk": self.course.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "алгебра")

    def test_course_update(self):
        """проверка изменения названия курса"""
        url = reverse("course:course-update", kwargs={"pk": self.course.pk})
        data = {"name": "алгебра (новое название)"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.get(pk=self.course.pk).name, "алгебра (новое название)")

    def test_course_destroy(self):
        """проверка удаления курса"""
        url = reverse("course:course-delete", kwargs={"pk": self.course.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)

    def test_questions_create(self):
        """проверка создания нового вопроса"""
        url = reverse("course:questions-create")
        data = {"question": "Какие числа больше 10?", "course": self.course.pk}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Questions.objects.count(), 2)

    def test_questions_list(self):
        """проверка получения списка всех вопросов"""
        url = reverse("course:questions-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["question"], "Что такое квадрат?")

    def test_questions_update(self):
        """проверка изменения вопроса"""
        url = reverse("course:questions-update", kwargs={"pk": self.questions.pk})
        data = {"question": "Что такое квадрат (новый вопрос)?"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Questions.objects.get(pk=self.questions.pk).question, "Что такое квадрат (новый вопрос)?")

    def test_questions_destroy(self):
        """проверка удаления вопроса"""
        url = reverse("course:questions-delete", kwargs={"pk": self.questions.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Questions.objects.count(), 0)

    def test_answers_create(self):
        """проверка создания нового ответа"""
        url = reverse("course:answers-create")
        data = {
            "question": self.questions.pk,
            "answer": "Число, умноженное на само себя",
            "correct": True,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answers.objects.count(), 2)

    def test_answers_list(self):
        """проверка получения списка всех ответов"""
        url = reverse("course:answers-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["answer"], "Число, умноженное на само себя")

    def test_answers_update(self):
        """проверка изменения ответа"""
        url = reverse("course:answers-update", kwargs={"pk": self.answers.pk})
        data = {"answer": "Число (новый ответ)"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Answers.objects.get(pk=self.answers.pk).answer, "Число (новый ответ)")

    def test_answers_destroy(self):
        """проверка удаления ответа"""
        url = reverse("course:answers-delete", kwargs={"pk": self.answers.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Answers.objects.count(), 0)

    def test_answer_student_create(self):
        """проверка создания нового ответа студента"""
        url = reverse("course:answer_student-create")
        data = {
            "answer": self.answers.pk,
            "question": self.questions.pk,
            "owner": self.user.pk,
            "is_correct": True,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AnswerStudent.objects.count(), 2)

    def test_answer_student_list(self):
        """проверка получения списка всех ответов студента"""
        url = reverse("course:answer_student-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["is_correct"], False)

    def test_answer_student_retrieve(self):
        """проверка получения конкретного ответа студента"""
        url = reverse("course:answer_student-retrieve", kwargs={"pk": self.answer_student.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["is_correct"], False)

    def test_answer_student_destroy(self):
        """проверка удаления ответа студента"""
        url = reverse("course:answer_student-delete", kwargs={"pk": self.answer_student.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AnswerStudent.objects.count(), 0)
