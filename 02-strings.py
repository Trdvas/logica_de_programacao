nome = "Thiego"

#caracteres de escape em srings
print("\n")

nome = "T\th\ti\te\tg\no"

print(nome)

#pode ser escrito com aspas simples
jogo = 'mortal kombat'

jogo = "mortal kombat" #e com aspas duplas também

#passando multiplos argumentos na função print
print(nome, jogo)

#aspas duplas e simples funcionam da mesma forma com a excesão de utilizar aspas dentro de uma string.
#aqui estão alguns exemplos da aplicação desta regra

aspas_simples = 'Ela disse "SIM"'
print(aspas_simples)

aspas_duplas = "Ela disse \"SIM\""
print(aspas_duplas)




#Notice that if you want to print \ you must put two
print("\\")

#voce pode prefixar a string com r que vai criar uma string bruta que ignora caracteres de escapte com execeção da mesma aspa utilizada na string
print(r'um exemplo prático.\'() \/\/. \t' ) #apenas \' foi escapado



########## concatenação ##########
item = str(5)
preço = str(15)
#Use o simbolo de + para somar duas strings
mensagem = item + " + " + preço
print(mensagem)

#pode usar virgula para separar os valores na função print
print(item, "+", preço)


#podemos usar multilinhas em strings
print("""Nome: Thiego
Idade: 22""")


########## INDICES ##########

#É muito comum selecionar um caractere especifico em uma string

msg = "É uma mensagem de teste"
print(msg[5]) 


#Esses valores podem ser atribuidos a uma variaável e ser utilizado em uma expressão
primeira_letra = msg[0]
print(primeira_letra)

#podemos selecionar o indíce do ultimo caractere
ultimo = msg[22] 
print(ultimo)
ultimo_indice_negativo = msg[-1] 
print(ultimo_indice_negativo)


########## SELEÇÃO DE CARACTERES #########

#repetindo a string para facilidade na leitura:
msg = "É uma mensagem de teste"

#podemos passar dois numeros no indice para obter uma série de caracteres
#o indice da esquerda é inclusivo e o da direita é exclusivo

print(msg[1:3]) 

#podemos deixar o primeiro indice vazio para selecionar desde o primeiro caractere
#ou deixar o segundo indice vazio para selecionar até o ultimo caractere
print(msg[:5]) 
print (msg[1:])

#podemos utilizar indices negativos para inverter a seleção do final para o início
print(msg[-8:]) #neste exemplo selecionamos os 8 ultimos caracteres



########## STRINGS SÃO IMUTÁVEIS ##########

#as strings nao podem ter os seus valoes alterados
nao_pode_mudar = "um texto aleatório"
#nao_pode_mudar[:3] = "pode"... Isso não pode ser feito em strings 

#podemos criar uma nova string a partir da primeira
linguagem = "Java é a minha linguagem favorita"
#Python é a minha linguagem favorita

linguagem_fav = "Python " + linguagem[4:]
print(linguagem_fav)
print(linguagem)


########## OBTER TAMANHO DE UMA STRING ##########

#existe uma função que podemos utilizar para retornar o tamanho de uma string

print(len(linguagem_fav))



