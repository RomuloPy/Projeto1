import random
from time import sleep

nomes = ['Nome', 'E-Mail', 'Telefone', 'Cidade', 'Estado']

opcoes = {
    '1': 'Nome',
    '2': 'E-Mail',
    '3': 'Telefone',
    '4': 'Cidade',
    '5': 'Estado'
}

boas_vindas = 'Bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa, digite "parar"'
print(boas_vindas)
print('-' * len(boas_vindas))
sleep(3)

while True:
    print('Escolha uma ou mais opções abaixo a serem geradas aleatoriamente')
    for opcao in opcoes:
        print(f'[{opcao}] - {nomes[int(opcao) - 1]}')
    escolhas = input('Digite uma ou mais opções separadas por vírgula (ex: 1,2,3): ').split(',')
    if 'parar' in escolhas:
        print('A encerrar o programa...')
        sleep(3)
        break
    salvar_txt = input('Deseja salvar os dados num arquivo de texto(.txt)? [S/N]')
    for escolha in escolhas:
        if escolha in opcoes:
            aleatorio = ''
            if opcoes[escolha] == 'Nome':
                aleatorio = random.choice(['Romulo', 'Rafael', 'Jason', 'Laura', 'Filomena', 'Antonio'])
            elif opcoes[escolha] == 'E-Mail':
                aleatorio = random.choice(['romulo@example.com', 'rafael@example.com',
                                            'jason@example.com', 'laura@example.com',
                                            'filomena@example.com', 'antonio@example.com'])
            elif opcoes[escolha] == 'Telefone':
                aleatorio = random.choice(['+351000000000', '+351111111111', '+351222222222',
                                            '+351444444444', '+351555555555', '+351666666666'])
            elif opcoes[escolha] == 'Cidade':
                aleatorio = random.choice(['Lisboa', 'Alenquer', 'Xira', 'Coimbra',
                                            'Aveiro', 'Porto'])
            elif opcoes[escolha] == 'Estado':
                aleatorio = random.choice(['California', 'Texas', 'Nova York', 'Florida', 'Illinois'])
            print(aleatorio)
            if salvar_txt.upper() == 'S':
                with open('dados.txt', 'a') as arquivo:
                    arquivo.write(aleatorio + '\n')
        else:
            print(f'\033[91mOpção inválida: {escolha}\033[0m')
