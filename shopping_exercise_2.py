print(" ") 
print("Bem-vindo ao Atacado Braian Vargas!!")
print(" ")
print("Tamanho " " Cupuaçu   " "  Açaí  ")
print("   P    " " R$ 9.00   " "R$ 11.00")
print("   M    " " R$ 14.00  " "R$ 16.00")
print("   G    " " R$ 18.00  " "R$ 20.00")
print(" ")

valor_total = 0
pede_pra_sair = False
# Loop para continuar perguntando até o usuário decidir parar
while True:
    if pede_pra_sair == True:
        break
    else:
        sabor = input("Escolha o sabor do seu sorvete (CP ou AC): ").lower()
    
#verificando qual o sabor e se o sabor é válido
    if sabor == "cp":
        tamanho = input("Escolha o tamanho do seu sorvete (P, M ou G): ").lower()
        if tamanho == "p":
            preco = 9
            valor_total += preco
        elif tamanho == "m":
            preco = 14
            valor_total += preco
        elif tamanho == "g":
            preco = 18
            valor_total += preco
        else:
            print("Tamanho inválido, tente novamente.")
            continue
        
# Abaixo é o preço do sorvete, junto do tamanho e valor unitário
        print("-" * 50)
        print(f"Você pediu cupuaçu no tamanho {tamanho.upper()}, que custa {preco} reais")
        print("-" * 50)

# Aqui é a pergunta se o cliente quer mais alguma coisa, + o valor total
        while True:    
            resposta = input("Deseja mais alguma coisa? (s/n) ").lower()
            print(" ")
            if resposta == "n":
                print(f"-------- Valor total a ser pago: R$ {valor_total:.2f} --------")
                print("Obrigado por comprar no Atacado Braian Vargas, volte sempre!!!!")
                print(" ")
                pede_pra_sair = True
                break
            elif resposta == "s":
                break
            else:
                print("Resposta inválida, tente novamente.")
                continue

    elif sabor == "ac":
        tamanho = input("Escolha o tamanho do seu sorvete (P, M ou G): ")
        if tamanho == "p":
            preco = 11
            valor_total += preco
        elif tamanho == "m":
            preco = 16
            valor_total += preco
        elif tamanho == "g":
            preco = 20
            valor_total += preco
        else:
            print("Tamanho inválido, tente novamente.")
            continue
        
        print("-" * 50)
        print(f"Você pediu açaí no tamanho {tamanho.upper()}, que custa {preco} reais")
        print("-" * 50)

        while True:    
            resposta = input("Deseja mais alguma coisa? (s/n) ").lower()
            print(" ")
            if resposta == "n":
                print(f"-------- Valor total a ser pago: R$ {valor_total:.2f} --------")
                print("Obrigado por comprar no Atacado Braian Vargas, volte sempre!!!!")
                print(" ")
                pede_pra_sair = True
                break
            elif resposta == "s":
                break
            else:
                print("Resposta inválida, tente novamente.")
                continue

    else:
        print("Sabor inválido, tente novamente.")
        continue