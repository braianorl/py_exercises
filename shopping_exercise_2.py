print("Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais")
print("Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais")
print("Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais")

valor_total = 0

while True:
    sabor = input("Escolha o sabor do seu sorvete (CP ou AC): ")
    
    if sabor == "cp":
        tamanho = input("Escolha o tamanho do seu sorvete (P, M ou G): ")
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
        
        print(f"Você pediu cupuaçu no tamanho {tamanho.upper()}, que custa {preco} reais")

        resposta = input("Deseja mais alguma coisa? (s/n)")
        if resposta == "n":
            print(f"Valor total a ser pago: {valor_total} reais")
            break
        elif resposta == "s":
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
        
        print(f"Você pediu açaí no tamanho {tamanho.upper()}, que custa {preco} reais")

        resposta = input("Deseja mais alguma coisa? (s/n)")
        if resposta == "n":
            print(f"Valor total a ser pago: {valor_total} reais")
            break
        elif resposta == "s":
            continue

    else:
        print("Sabor inválido, tente novamente.")
        continue