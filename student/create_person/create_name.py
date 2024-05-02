from pi1tg18.settings.base import BASE_DIR
from random import choice, randint

# Função gerar nomes


def get_names(arquivo):
    local = BASE_DIR / arquivo
    arquivo_txt = local
    print(arquivo_txt)

    names = []  # inicia uma lista vazia
    with open(arquivo_txt, 'r') as file:  # abre o arquivo com a função with
        name = file.readline()  # um interavel para ler linha a linha
        names = []
        while name:  # loop identificar o nome em cada linha
            # adiciona o nome da linha na lista
            names.append(name.strip('\n',).title())
            name = file.readline()
    return names  # retorna o resultado


def gerar_sobrenome():
    lista = last_names

    composto = (True, False)

    if composto:
        last_name = f'{choice(lista)} {choice(lista)}'
    else:
        last_name = f'{choice(lista)}'

    return f'{last_name}'


def gerar_telefone():
    telefone = '9'
    for i in range(8):
        telefone += str(randint(0, 9))

    return telefone


def gerar_endereco():
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


def __gerar_nome(lista: list):
    lista = lista

    composto = (True, False)

    if choice(composto):
        nome = f'{choice(lista)} {choice(lista)}'
    else:
        nome = f'{choice(lista)}'

    return f'{nome}'


def gerar_nome_masculino():

    return __gerar_nome(male_list)


def gerar_nome_feminino():

    return __gerar_nome(female_list)


def gerar_nome_aleatorio():
    listas = (male_list, female_list)
    return __gerar_nome(choice(listas))


def gerar_nomes(quantidade: int = 1):

    nomes = []
    for i in range(quantidade):
        nome = gerar_nome_aleatorio()
        nomes.append(nome)

    return nomes


male_list = get_names('names_males.txt')
female_list = get_names('names_females.txt')
last_names = get_names('sobrenomes.txt')
hosts = ['hotmail.com', 'live.com', 'microsoft.com',
         'gmail.com', 'icloud.com', 'bol.com.br', 'yahoo.com']

if __name__ == "__main__":
    print('funcionando')
