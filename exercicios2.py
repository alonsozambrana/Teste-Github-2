#1
prato_do_dia=35 
prato_almoço=25
economia=prato_do_dia-prato_almoço
print(f"pedindo no horario do almoço uma pessoa economizaria:{economia} reais")

#2
base=8
altura=6
area=base*altura
print(area)

#3
base=float(input("digite a base do retangulo:\n"))
altura=float(input("digite a altura do retangulo:\n"))
area=base*altura
print(f"a area do retangylo sera de ",area)

#4
peso=float(input("digite o peso da pessoa:\n"))
altura=float(input("digite a altura da pessoa:\n"))
imc=peso/(altura**2)
print(f"o seu indice de massa corporal é:{imc}")

#5
distancia=float(input("digite a distancia que irá percorrer:\n"))
velocidade=float(input("digite a velocidade media do veiculo:\n"))
tempo_de_viagem=distancia//velocidade
print(f"o tempo total de viagem será de:{tempo_de_viagem}")


promocao=("promoção: 20% de desconto")
print(promocao)
peca=float(input("digite o valor da peça de roupa:\n"))
desconto=(peca/100)*20
valor_final=peca-desconto
print(f"o valorfinal a ser pago com o desconto sera de :{valor_final}")


lado=6
formula=(6**2)*(3*0.5)/4
print(f"a area de um triangulo equilatero de lado 6 é:{formula}")


isadora=("isaodra recebe 702 reais por mês")
print(isadora)
conta=702.00
contas=float(input("digite o valor total das contas que deve pagar:\n"))
saldo=conta-contas
print(f"o saldo restante na conta corrente de isadora é:{saldo}" )