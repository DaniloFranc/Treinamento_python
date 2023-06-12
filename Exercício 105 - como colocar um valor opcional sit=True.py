def notas(*number, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param number: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    cont = 0
    maior = 0
    media = 0
    soma = 0
    menor = 1000
    dict = {}
    for c in number:
        cont = cont + 1
        soma = soma + c
        if maior < c:
            maior = c
        if menor > c:
            menor = c
    media = (soma/cont)

    dict = {'total': cont, 'maior': maior, 'menor': menor, 'media': media}

    if sit == True and media >= 7:
        dict = {'total': cont, 'maior': maior, 'menor': menor, 'media': media, 'situação': 'BOA'}
    if sit == True and 6 <= media < 7:
        dict = {'total': cont, 'maior': maior, 'menor': menor, 'media': media, 'situação': 'RAZOÁVEL'}
    if sit == True and 4 <= media < 6:
        dict = {'total': cont, 'maior': maior, 'menor': menor, 'media': media, 'situação': 'RUIM'}
    return dict






n = notas(3.5,2,6.5,10,10,10,sit=False)
print(n)
#help(notas)

