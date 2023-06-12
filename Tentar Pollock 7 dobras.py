co = 0
while co == 0:
    peso = float(input('Digite o seu peso: '))
    su = float(input('Digite o valor da dobra Subescapular: '))
    tri = float(input('Digite o valor da dobra Tricipial: '))
    am = float(input('Digite o valor da dobra Axilar Média: '))
    si = float(input('Digite o valor da dobra Supra-ilíaca: '))
    pt = float(input('Digite o valor da dobra Peitoral: '))
    ab = float(input('Digite o valor da dobra Abdominal: '))
    co = float(input('Digite o valor da dobra Coxar: '))

a = (1.112 - 0.00043499*(su+tri+am+si+pt+ab+co)+ 0.00000055*(su+tri+am+si+pt+ab+co)**2 - 0.00028826*32)
b = 495/a - 450

massag = peso*(b/100)
massam = peso - massag




print('\n Você está com {:.2f}% de gordura corporal\n a sua massa muscular é: {:.2f}\n e sua massa em gordura é: {:.2f}'.format(b,massam,massag))