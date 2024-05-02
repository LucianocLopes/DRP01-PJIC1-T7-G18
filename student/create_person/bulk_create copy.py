from .pessoa import pessoa
from student.models import Student

student_list = pessoa(300)

student = [student(
    registered=student['registered'],
    first_name=student['first_name'],
    last_name=student['last_name'],
    mother_name=student['mother_name'],
    father_name=student['father_name'],
    phone_ddd=student['phone_ddd'],
    phone_number=student['phone_number'],
    email=student['email'],
    address_zipcode=student['address_zipcode'],
    address=student['address'],
    address_number=student['address_number'],
    address_complement=student['address_complement'],
    address_district=student['addess_district'],
    address_city=student['address_city'],
    address_state=student['address_state'],
) for student in student_list]

Student.objects.bulk_create(student)

if __name__ == "__main__":
    print('funcionando')
