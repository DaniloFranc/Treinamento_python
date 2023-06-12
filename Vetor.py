# Python2 para 'print' sem pular linha : print("*" , end = "");
from __future__ import print_function

n = 10;

# Definir vetor/lista com: (10,11,12,13,...10+n-1)
vet = []; # define um vetor vazio
for i in range(0, n, 1) : # ou mais simples neste caso "for i in range(n)"
  vet.append(10+i); # anexe mais um elemento `a lista
# Imprime o vetor/lista de uma so' vez (na mesma linha)
print("\nO vetor: ", end=""); # informe o que vira impresso a seguir (na mesma linha devido ao parametro end=""
print(vet);

# Imprimir vet em linha unica na forma "( 0,  0) ( 1,   1)..."
print("\nNovamente o vetor impresso de 2 modos: "); # informe o que vira impresso a seguir (e "quebre" a linha)
i = 0;
for item in vet : # "item in vet" e' um iterador, item comeca em vet[0], depois vet[1] e assim por diante
  print("(%2d, %2d) " % (item, vet[i]), end="");
  i += 1;
print(); # quebre a linha