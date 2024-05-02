from pessoa import list_students
from student.models import Student
from django.contrib.auth import get_user_model

User = get_user_model()


def lista_pessoas(quantidade):
    student_list = list_students(quantidade)
    obj_list = [Student(**student_dict) for student_dict in student_list]
    objs = Student.objects.bulk_create(obj_list)
    objs
    return 'ok'
