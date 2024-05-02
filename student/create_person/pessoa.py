import csv
import uuid
from django.contrib.auth import get_user_model
from random import choice, randint
from .create_name import __gerar_nome, hosts, male_list, gerar_nome_aleatorio, \
    gerar_nome_feminino, gerar_nome_masculino, gerar_sobrenome, gerar_telefone

User = get_user_model()


def pessoa() -> dict:
    registered = False
    mother = gerar_nome_feminino()
    mother_lastname = gerar_sobrenome()
    father = gerar_nome_masculino()
    father_lastname = gerar_sobrenome()
    first_name = gerar_nome_aleatorio()
    last_name = f'{mother_lastname.split()[-1]} {father_lastname.split()[-1]}'
    email = f'{first_name.lower().replace(' ', '')}_{
        last_name.lower().replace(' ', '')}@{choice(hosts)}'
    ddd = '11'
    phone = gerar_telefone()
    cep = '08'
    for i in range(6):
        cep += str(randint(0, 9))

    tipo = ('Rua', 'Avenida', 'Estrada', 'Viela', 'Praça')
    lougradouro = choice(tipo)

    endereco = __gerar_nome(male_list)

    for i in range(5):
        numero = ""
        num = randint(0, 9)
        if not num == 0 and numero == "":
            numero += str(num)

    letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

    complement = ('casa', f'bloco: {randint(1, 50)} Apto: {randint(1, 500)}', f'bloco: {choice(letras)} Apto: {randint(1, 500)}', f'Apto: {
                  randint(1, 500)}{choice(letras)}', f'casa: {choice(letras)}', f'casa:{randint(1, 500)}{choice(letras)}', 'fundos')
    complemento = choice(complement)

    district = ('Santo', 'Jardim', 'Parque', 'Vila')
    bairro = f'{choice(district)} {choice(male_list)}'

    city = ('Suzano', 'Poa', 'Mogi das Cruzes',
            'Itaquaquecetuba', 'Riberão Pires')
    cidade = choice(city)

    estado = 'SP'

    obj = {
        'user': User.objects.all().first(),
        'registered': registered,
        'first_name': first_name,
        'last_name': last_name,
        'mother_name': f'{mother} {mother_lastname}',
        'father_name': f'{father} {father_lastname}',
        'email': email,
        'phone_ddd': ddd,
        'phone_number': phone,
        'address_zipcode': cep,
        'address': f'{lougradouro} {endereco}',
        'address_number': numero,
        'address_complement': complemento,
        'address_district': bairro,
        'address_city': cidade,
        'address_state': estado,
    }
    return obj


def list_students(quantidade: int = 1):
    students = list()
    for i in range(quantidade):
        aluno = pessoa()
        students.append(aluno)
    return students


if __name__ == "__main__":
    print('funcionando')
