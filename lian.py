

#questão 5


"""N = float(input("Digite um número: "))

if N > 0:
    print("O número é positivo.")
elif N < 0:
    print("O número é negativo.")
else:
    print("O número é nulo.")"""

#questão 6

"""numero = int(input("Digite o número: "))


calculo = (numero%3)


if calculo == 0:
     print("Multiplo")
else:
     print("Não é multiplo")"""

#questão 7


"""nosso_numero = int(input("insira um numero:"))


eh_divisivel_por_3 = False
eh_divisivel_por_5 = False

if nosso_numero % 3 == 0:
    eh_divisivel_por_3 = True

if nosso_numero % 5 == 0:
    eh_divisivel_por_5 = True


if eh_divisivel_por_3 and eh_divisivel_por_5:
    print("O número %d é divisível por 3 e 5" % nosso_numero)
elif eh_divisivel_por_3:
    print("O número %d é divisível por 3." % nosso_numero)
elif eh_divisivel_por_5:
    print("O número %d é divisível por 5." % nosso_numero)
else:
    print("O número %d não é divisível por 3 nem por 5." % nosso_numero)
"""

#questão 8


"""A = float(input('Digite o número A: '))
B = float(input('Digite o número B: '))

if B == 0:
    print('Não há divisão por 0')
else:
    if A % B == 0:
        print(f'{A} é divisível por {B}')
    else:
        print(f'{A} não é divisível por {B}')"""


#questão 9

"""def peso_ideal(alt, sexo):

 if sexo == 'f':


  print(f'Seu peso ideal é {62.1*alt- 44.7:.1f}kg')

 elif sexo == 'm':
 
  print(f'Seu peso ideal é {72.7*alt-58:.1f}kg')

 else:

  print('erro identificado.')




altura = float(input('Digite sua altura: '))

sexo = str(input('Sexo [F/M]: ')).strip().lower()
 
peso_ideal(altura, sexo)"""



#questão 10

"""a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor "))

maior = a
menor = a

if b > maior:
    maior = b
if c > maior:
    maior = c

if b < menor:
    menor = b
if c < menor:
    menor = c

print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")"""

#questão 25

def middle(lista):
   return lista[1:-1]

lista_original = [1, 2, 3, 4, 5]
nova_lista = middle(lista_original)
print(nova_lista)