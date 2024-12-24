from django.urls import path

from course.apps import CourseConfig
from course.views import (AnswersDestroyAPIView, AnswersListAPIView,
                          AnswersUpdateAPIView, CourseCreateAPIView,
                          CourseDestroyAPIView, CourseListAPIView,
                          CourseRetrieveAPIView, CourseUpdateAPIView,
                          QuestionsDestroyAPIView, QuestionsListAPIView,
                          QuestionsUpdateAPIView)

app_name = CourseConfig.name


urlpatterns = [
    path("", CourseListAPIView.as_view(), name="course-list"),
    path("create/", CourseCreateAPIView.as_view(), name="course-create"),
    path("<int:pk>/", CourseRetrieveAPIView.as_view(), name="course-retrieve"),
    path("<int:pk>/update/", CourseUpdateAPIView.as_view(), name="course-update"),
    path("<int:pk>/delete/", CourseDestroyAPIView.as_view(), name="course-delete"),
    path("questions/", QuestionsListAPIView.as_view(), name="questions-list"),
    path(
        "questions/<int:pk>/update/",
        QuestionsUpdateAPIView.as_view(),
        name="question-update",
    ),
    path(
        "questions/<int:pk>/delete/",
        QuestionsDestroyAPIView.as_view(),
        name="question-delete",
    ),
    path(
        "questions/<int:pk>/answers", AnswersListAPIView.as_view(), name="answers-list"
    ),
    path(
        "questions/<int:pk>/answers/<int:answer_pk>/update/",
        AnswersUpdateAPIView.as_view(),
        name="answers-update",
    ),
    path(
        "questions/<int:pk>/answers/<int:answer_pk>/delete/",
        AnswersDestroyAPIView.as_view(),
        name="answers-delete",
    ),
]
