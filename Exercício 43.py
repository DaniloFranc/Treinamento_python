peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso/altura**2

if imc < 18.5:
    print('você está abaixo do peso! {:.3f}'.format(imc))
elif 18.5 <= imc < 25:
    print('peso ideal! {:.3f}'.format(imc))
elif 25 <= imc < 30:
    print('você está com Sobrepeso! {:.3f}'.format(imc))
elif 30 <= imc < 40:
    print('você está Obeso! {:.3f}'.format(imc))
elif imc > 40:
    print('Você está com Obesidade Morbida! {:.3f}'.format(imc))
