# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print(f'Hello world')

#2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = int(input('Por favor, me diga um número: '))

print(f'O número informado foi {numero}.')

#3. Faça um Programa que peça dois números e imprima a soma.
primeiro_numero = int(input('Me diga um número: '))
segundo_numero = int(input('Ótimo. Agora me diga o segundo número: '))

soma = primeiro_numero + segundo_numero

print(f'A soma dos números é {soma}.')

#4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.
primeira_nota = float(input('Por favor, insira a primeira nota: '))
segunda_nota = float(input('Agora, me diga a segunda nota: '))
terceira_nota = float(input('Insira a terceira nota: '))
quarta_nota = float(input('Por último, a quarta nota: '))

total = primeira_nota + segunda_nota + terceira_nota + quarta_nota

media = total / 4

print(f'A mestra bimestral que você teve foi de {media}.')

#5. Faça um Programa que converta metros para centímetros.
metro = float(input('Insira o número de metros para serem convertidos: '))

centimetro = 100 * metro

print(f'O valor de {metro} metro(s) convertido será de {centimetro} cm.')

#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input('Por favor, insira o raio do círculo: '))

a = math.pi * (raio**2)

print(f'A área é de {a:.2f} cm.')

#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input('Insira um valor para o lado em centímetros: '))
area = lado * lado

dobro_area = area * 2

print(f'O valor do dobro da área do quadrado é de {dobro_area} cm.')

#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input('Quanto você ganha por hora? Diga aqui: '))
dia_trabalhado = 8 * hora
mes_trabalhado = 22 * dia_trabalhado

print(f'Supondo que você trabalha por 22 dias úteis ao mês, você recebe R${mes_trabalhado} de dinheiro.')

#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input('Me diga a temperatura em Fahrenheit: '))
celsius = 5 * ((fahrenheit - 32) / 9)

print(f'A temperatura em Celsius é de {celsius:.1f} graus')

#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input('Me diga a temperatura em Celsius: '))
fahrenheit = ((9 * celsius / 5)) + 32

print(f'A temperatura em Fahrenheit é de {fahrenheit:.1f} graus')

#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

int1 = int(input('Insira o primeiro número inteiro: '))
int2 = int(input('Insira o segundo número inteiro: '))
real = float(input('Insira um número real: '))

prod_dobro_primeiro_metade_segundo = (int1 * 2) * (int2 / 2)
soma_triplo_primeiro_terceiro = (int1 * 3) + real
terceiro_cubo = (real ** 3)

print(f'O produto do dobro do primeiro com metade do segundo é de {prod_dobro_primeiro_metade_segundo}. \nA soma do triplo do primeiro com o terceiro é de {soma_triplo_primeiro_terceiro}. \nO terceiro elevado ao cubo é de {terceiro_cubo}.')

#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Insira a sua altura aqui: '))
peso_ideal = (72.7 * altura) - 58

print(f'Seu peso ideal é de {peso_ideal} kg.')

#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Insira a sua altura: '))
homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

print(f'Caso você seja um homem, o seu peso ideal é de {homens}. \nCaso você seja uma mulher, o seu peso ideal é de {mulheres}.')

# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Insira o peso dos peixes: '))
excesso = peso - 50
variavel = 4 * excesso

print(f' O peso foi de {peso:.2f}. O excesso foi de {excesso:.2f}. Ou seja, a taxa que João vai pagar é de {variavel:.2f}')

# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salario_hora = float(input('Insira o valor que você ganha por hora: '))
horas_mes = int(input('Insira o número de horas que você trabalhou no mês: '))
salario_bruto = salario_hora * horas_mes

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sindicato

print(f'O salário bruto foi de R${salario_bruto:.2f}. \nVocê pagou ao INSS o valor de R${inss:.2f}. \nPara o sindicato, R${sindicato:.2f}. \nE, por fim, seu salário foi de R${salario_liquido}. Kinda sad, innit?')

#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input('Coloque aqui a área em metros quadrados: '))
litros = area / 3
latas = litros / 18

latas = int(latas)
if litros % 18 != 0:
    latas += 1

preco = 80 * latas

print(f'A quantidade necessária é de {latas} latas e o preço é de R${preco:.2f}.')

