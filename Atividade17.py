# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.
ano = int(input("Ano: "))
if (ano % 4 ) == 0:
    print (f"{ano} é um ano bissexto")
else:
    print (f"{ano} não é um ano bissexto")
