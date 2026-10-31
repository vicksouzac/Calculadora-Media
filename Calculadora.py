#Calculadora de Media Escolar 


while True:
    NOTA1 = float(input("digite a primeira nota: "))
    NOTA2 = float(input("digite a segunda nota: "))
    NOTA3 = float(input("digite a terceira nota: "))
    NOTA4 = float(input("digite a quarta nota: "))
    media = (NOTA1 + NOTA2 + NOTA3 + NOTA4) / 4
    if media >= 7:
            print("Parabéns, você foi aprovado com a media: ", media )
    elif media >= 4.5:
            print("Você está de recuperação com a media: ", media )
    else:
            print("Você foi repravado com a media: ", media )

    #Pergunta de sim ou não para fazer outro calculo 
    resposta = input("Deseja fazer outro calculo? (sim ou não): ")

    #Se a resposta for sim, o programa reinicia, caso contrário, ele encerra.
    if resposta not in ("sim", "s", "SIM", "S"):
            print("Obrigado por usar a calculadora de media escolar!")
            break 

