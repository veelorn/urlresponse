import requests

branco=('\033[1;30m')
vermelho=('\033[1;31m')
verde=('\033[1;32m')
amarelo=('\033[1;33m')
azulclaro=('\033[1;34m')
roxo=('\033[1;35m')
verdeagua=('\033[1;36m')
cinza=('\033[1;37m')
brancob=('\033[1;30;40m')
vermelhob=('\033[1;31;40m')
verdeb=('\033[1;32;40m')
amarelob=('\033[1;33;40m')
azulclarob=('\033[1;34;40m')
roxob=('\033[1;35;40m')
verdeaguab=('\033[1;36;40m')
cinzab=('\033[1;37;40m')
brancovermelho=('\033[1;30;41m')
vermelhovermelho=('\033[1;31;41m')
verdevermelho=('\033[1;32;41m')
amarelovermelho=('\033[1;33;41m')



print(f'\n{amarelo}▄• ▄▌▄▄▄  ▄▄▌      ▄▄▄  ▄▄▄ ..▄▄ ·  ▄▄▄·       ▐ ▄ .▄▄ · ▄▄▄ .')
print('█▪██▌▀▄ █·██•      ▀▄ █·▀▄.▀·▐█ ▀. ▐█ ▄█▪     •█▌▐█▐█ ▀. ▀▄.▀·')
print('█▌▐█▌▐▀▀▄ ██▪      ▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄ ██▀· ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄▐▀▀▪▄')
print('▐█▄█▌▐█•█▌▐█▌▐▌    ▐█•█▌▐█▄▄▌▐█▄▪▐█▐█▪·•▐█▌.▐▌██▐█▌▐█▄▪▐█▐█▄▄▌')
print(' ▀▀▀ .▀  ▀.▀▀▀     .▀  ▀ ▀▀▀  ▀▀▀▀ .▀    ▀█▄▀▪▀▀ █▪ ▀▀▀▀  ▀▀▀  \033[m')

print(f'\n{verde}PERCORRENDO URL EM LISTA REALIZANDO TESTE DE RESPOSTA HTTP\033[m')
print(f'                 by {vermelho}@veelorn\033[m {roxo}(Hack Tool)\033[m\n')

print(f'{cinza}http://exemplo.com/id=\033[m{verde}1100\033[m{cinza}logIn/\033[m')
print(f'{cinza}http://exemplo.com/id=\033[m{verde}1101\033[m{cinza}logIn/\033[m')
print(f'{cinza}http://exemplo.com/id=\033[m{verde}1102\033[m{cinza}logIn/\033[m')

start = int(input('\nInsira o Valor Inicial: '))
stop = int(input('Insira o valor final: '))
url = input('Insira a URL até onde ela será fixa: ')
diretorios = range(start,stop+1)
extensao = input('Há continuadade de caracteres ou alguma extensão?\nEx: [.png][.jpeg][.txt]\nCaso não haja, pressione Enter: ')
print('\n')
for pasta in diretorios:
    teste = (url)+str(pasta)+str(extensao)
    requisicao = requests.get(teste)
    if requisicao.status_code >= 100 and requisicao.status_code <= 199:
        print(f'{azulclaro}Resposta de Informação | \033[m'+ teste)
    elif requisicao.status_code >= 200 and requisicao.status_code <=299:
        print(f'{verde}Resposta de Sucesso | \033[m'+ teste)
    elif requisicao.status_code >= 300 and requisicao.status_code <=399:
        print(f'{amarelo}Redirecionamentos | \033[m'+ teste)
    elif requisicao.status_code >= 400 and requisicao.status_code <=499:
        print(f'{vermelhob}Erro de Cliente | \033[m'+ teste)
    elif requisicao.status_code >= 500 and requisicao.status_code <=599:
        print(f'{vermelho}Erro de Servidor | \033[m'+ teste)
    else:
        print('Código desconhecido | '+ teste)
print('\n')

requests