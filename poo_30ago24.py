# -*- coding: utf-8 -*-
"""POO_30AGO24

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BxJLPsIVNTt3Ssx_7nslXo-MuS7Om0uN

EX1) Converter F para C obs: Entrada F processamento: C = (5/9)(F-32) Saida: C
"""

F = float(input("Digite valor em Graus Farenheit: "))
C=(5/9) * (F-32)
print("Graus Celsius: ", C)

"""METODO PRINTF
print(f" ") se coloca o f no começo dos parenteses e antes das aspas e tem que colocar a variavel em {F} para aparecer na mensagem
"""

F = float(input("Digite valor em Graus Farenheit: "))
C=(5/9) * (F-32)
print(f"o valor de {F} em Graus Celsius: ", C)

"""EX2) Converter Polegadas para mm
Entrada: P
Processamento: MM = P * 25.4
Saida: MM
"""

P = float(input("Digite valor em Polegadas: "))
MM = P * 25.4
print(f"O valor de {P} Polegadas corresponde ao valor de {MM} mm")

"""EX3) Converter Milimetros para Polegadas
Entrada: MM
Processamento: P = MM / 25.4
Saida: P
"""

MM = float(input("Digite valor em Polegadas: "))
P = MM / 25.4
print(f"O valor de {MM} Milímetros corresponde ao valor de {P} Polegadas")

"""EX4 Solicitar a idade do Usuario
Entrada: Idade
Processamento: <= 16 e < 70
Saida: "Pode votar ou não"
"""

I = int(input("Digite a sua idade: "))

if 16 <= I < 70:
    print(f"A sua Idade {I} anos esta na Faixa etaria de 16 a 70 anos. ")
else:
    print(f"A sua Idade {I} anos esta fora da Faixa etaria de 16 a 70 anos. ")

I = int(input("Digite a sua idade: "))

if I >= 18:
    print("Pode Votar")
else:
    print("Não Pode Votar")