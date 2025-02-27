from django.urls import path

from course.apps import CourseConfig
from course.views import (AnswersCreateApiView, AnswersDestroyApiView,
                          AnswersListApiView, AnswerStudentCreateApiView,
                          AnswerStudentDestroyApiView,
                          AnswerStudentListApiView,
                          AnswerStudentRetrieveApiView, AnswersUpdateApiView,
                          CourseCreateApiView, CourseDestroyApiView,
                          CourseListApiView, CourseRetrieveApiView,
                          CourseUpdateApiView, QuestionsCreateApiView,
                          QuestionsDestroyApiView, QuestionsListApiView,
                          QuestionsUpdateApiView)

app_name = CourseConfig.name


urlpatterns = [
    path("course/", CourseListApiView.as_view(), name="course-list"),
    path("course/create/", CourseCreateApiView.as_view(), name="course-create"),
    path("course/<int:pk>/", CourseRetrieveApiView.as_view(), name="course-retrieve"),
    path(
        "course/<int:pk>/update/", CourseUpdateApiView.as_view(), name="course-update"
    ),
    path(
        "course/<int:pk>/delete/", CourseDestroyApiView.as_view(), name="course-delete"
    ),
    path("questions/", QuestionsListApiView.as_view(), name="questions-list"),
    path(
        "questions/create/", QuestionsCreateApiView.as_view(), name="questions-create"
    ),
    path(
        "questions/<int:pk>/update/",
        QuestionsUpdateApiView.as_view(),
        name="questions-update",
    ),
    path(
        "questions/<int:pk>/delete/",
        QuestionsDestroyApiView.as_view(),
        name="questions-delete",
    ),
    path("answers/", AnswersListApiView.as_view(), name="answers-list"),
    path(
        "answers/create/",
        AnswersCreateApiView.as_view(),
        name="answers-create",
    ),
    path(
        "answers/<int:pk>/update/",
        AnswersUpdateApiView.as_view(),
        name="answers-update",
    ),
    path(
        "answers/<int:pk>/delete/",
        AnswersDestroyApiView.as_view(),
        name="answers-delete",
    ),
    path(
        "answer_student/create/",
        AnswerStudentCreateApiView.as_view(),
        name="answer_student-create",
    ),
    path(
        "answer_student/",
        AnswerStudentListApiView.as_view(),
        name="answer_student-list",
    ),
    path(
        "answer_student/<int:pk>/",
        AnswerStudentRetrieveApiView.as_view(),
        name="answer_student-retrieve",
    ),
    path(
        "answer_student/<int:pk>/delete/",
        AnswerStudentDestroyApiView.as_view(),
        name="answer_student-delete",
    ),
]
