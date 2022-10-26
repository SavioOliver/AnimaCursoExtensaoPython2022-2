#Comando input() serve para solicitar para o usuario digitar algo.
#desta forma não guarda a informação inserida.
#input("Usuario por favor digite seu nome: ") 
#desta forma guarda a informação inserida.
nome = input("Usuario por favor digite seu nome: ")
idade = int(input ("Digite sua idade: "))
#comando de saida para exibir na tela
print (f"Seu nome é: {nome}")
print ("Sua idade é:{}".format(idade))
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))