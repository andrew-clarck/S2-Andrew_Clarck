#-*- coding: UTF-8 -*-
while True:
        
    print("Esse programa irá funcionar como calculadora, você escolhe dois números e a operação que quer realizar. É importante citar que a operação será realizada na ordem que você digitar os valores.")
    parar = int(input("Se quiser parar com o programa, digite 1, caso contrário, digite qualquer outro número: "))

    if parar == 1:
        print("Você escolheu parar.")
        break
    else:
        v1 = float(input("Digite o primeiro valor: "))
        v2 = float(input("Digite o segundo valor: "))
        operador = input("Digite a operação que quer realizar, + para soma, - para subtração, / para divisão e * para multiplicação: ")

        def soma(v1,v2,operador):
            soma = v1 + v2
            return soma


        def subtracao(v1,v2,operador):
            subtracao = v1 - v2
            return subtracao
        

        def divisao(v1,v2,operador):
            divisao = v1 / v2
            return divisao


        def multiplicacao(v1,v2,operador):
            multiplicacao = v1 * v2
            return multiplicacao


        if operador == "+":
            print(f"{v1} + {v2} = ", soma(v1,v2,operador))
            
        elif operador == "-":
            print(f"{v1} - {v2} = ", subtracao(v1,v2,operador))

        elif operador == "/":
            print(f"{v1} / {v2} = ", divisao(v1,v2,operador))

        elif operador == "*":
            print(f"{v1} * {v2} = ", multiplicacao(v1,v2,operador))

        else:
            print("Você digitou um operador inválido, tente novamente.")