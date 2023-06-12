ano = int(input('Digite o ano do seu nascimento: '))

prazo = 2023 - ano

if prazo > 18:
    print('Já passou do tempo do alistamento em {} anos'.format(prazo - 18))
elif prazo < 18:
    print('Você ainda vai se alistar em {} anos'.format(18 - prazo))
elif prazo == 18:
    print('Está na hora de você se alistar!')