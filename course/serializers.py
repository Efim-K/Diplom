from rest_framework.serializers import ModelSerializer, SerializerMethodField, ReadOnlyField

from course.models import Answers, AnswerStudent, Course, Questions
from course.validators import AnswerStudentValidators


class QuestionsSerializer(ModelSerializer):
    """Serializer для вопроса"""
    answers = SerializerMethodField()

    def get_answers(self, instance):
        """Возвращает список id ответов в вопросе теста"""
        return [{"id": obj.id, "answer": obj.answer} for obj in Answers.objects.filter(question=instance)]

    class Meta:
        model = Questions
        exclude = ["owner", ]
        ordering = ["question", "answer"]


class AnswersSerializer(ModelSerializer):
    """Serializer для ответа"""

    class Meta:
        model = Answers
        fields = "__all__"


class AnswerStudentSerializer(ModelSerializer):
    """Serializer для ответа"""
    info_course = SerializerMethodField()

    def get_info_course(self, instance):
        """Возвращает информацию о курсах"""

        for course in Questions.objects.filter(course=instance.answer.question.course):
            if instance.count_of_question != 0:
                course = instance.answer.question.course
                percent_correct = instance.count_of_correct * 100 / instance.count_of_question
                result = {"id": course.id, "Название темы": course.name,
                          "Кол-во отвеченных вопросов": instance.count_of_question,
                          "Кол-во правильных ответов": instance.count_of_correct,
                          "Процент правильных ответов": percent_correct,
                          }
                return result
            else:
                course = instance.answer.question.course
                result = {"id": course.id, "Название темы": course.name,
                          "Кол-во отвеченных вопросов": instance.count_of_question
                          }
                return result

    class Meta:
        model = AnswerStudent
        fields = "__all__"
        # read_only_fields = ["owner",]
        validators = [AnswerStudentValidators()]


class CourseSerializer(ModelSerializer):
    """Serializer для вопросов курса"""

    count_of_questions = SerializerMethodField()
    questions = SerializerMethodField()
    answer_students = AnswerStudentSerializer(many=True, read_only=True)

    def get_questions(self, course):
        """Возвращает список вопросов курса"""

        return [{"id": obj.id, "question": obj.question} for obj in Questions.objects.filter(course=course)]

    def get_count_of_questions(self, course):
        """Возвращает количество вопросов в курсе"""

        return Questions.objects.filter(course=course).count()

    # def get_answer_students(self, instance):
    #
    #
    #     return {"Кол-во отвеченных вопросов": AnswerStudent.count_of_question,
    #             "Кол-во правильных ответов": AnswerStudent.count_of_correct,
    #     }

    class Meta:
        model = Course
        # fields = ['id', 'name', 'description', 'count_of_questions', 'questions', 'answer_students', "owner"]
        fields = '__all__'
