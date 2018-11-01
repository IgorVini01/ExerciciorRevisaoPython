pessoa1 = input("Telefonou para a vítima ? ")
pessoa2 = input("Esteve no local ? ")
pessoa3 = input("Mora perto da vítima ? ")
pessoa4 = input("Devia para a vítima ? ")
pessoa5 = input("Já trabalhou com a vítima ? ")

cont = 0

if pessoa1 == "sim":
    cont = cont + 1
if pessoa2 == "sim":
    cont = cont + 1
if pessoa3 == "sim":
    cont = cont + 1
if pessoa4 == "sim":
    cont = cont + 1
if pessoa5 == "sim":
    cont = cont + 1

if cont == 1:
    print("Inocente")
    
if cont == 2:
    print("Suspeita")
if cont == 3:
    print("Cúmplice")
if cont == 4:
    print("Cúmplice")
if cont == 5:
    print("Assassino")
if cont == 0:
    print("Inocente")
