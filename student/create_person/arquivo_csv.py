from pi1tg18.settings.base import BASE_DIR
import csv
from student.create_person.pessoa import list_students


def gravar_csv(arquivo='MeuCSV.csv', quantidade: int = 1):
    local = BASE_DIR / 'create_person/'
    arquivo_csv = local & arquivo
    print(arquivo_csv)

    field_names = [
        'first_name',
        'last_name',
        'mother_name',
        'faher_name',
        'email',
        'phone_ddd',
        'phone_number',
        'address_zipcode',
        'address',
        'address_number',
        'address_complemt',
        'address_district',
        'address_city',
        'address_state'
    ]
    students = list_students(quantidade)

    with open(arquivo_csv, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(students)


if __name__ == "__main__":
    print('funcionando')
    gravar_csv(500)
