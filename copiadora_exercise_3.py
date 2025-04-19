def escolha_servico(): # Valida o serviço escolhido pelo usuário e retorna o valor do serviço escolhido
    while True: 
        print("Serviços disponíveis:")
        print("DIG - Digitalização: R$ 1,10")
        print("ICO - Impressão Colorida: R$ 1,00")
        print("IPB - Impressão Preto e Branco: R$ 0,40")
        print("FOT - Fotocópia: R$ 0,20")
        print(" ")
        servico = input("Digite o serviço desejado (DIG, ICO, IPB ou FOT): ").upper()
        if servico == "DIG":
            return 1.10
        elif servico == "ICO":
            return 1.00
        elif servico == "IPB":
            return 0.40
        elif servico == "FOT":
            return 0.20
        else:
            print("Serviço inválido, tente novamente.")
            print(" ")
            continue

def num_paginas(): # Valida o número de páginas e aplica desconto se necessário
    while True:
        try:
            paginas = int(input("Digite o número de páginas: "))
            if paginas > 0 and paginas < 20:
                return paginas
            elif paginas >= 20 and paginas < 200:
                paginas = paginas-(paginas*0.15)
                return int(paginas) # arredonda páginas para número inteiros
            elif paginas >= 200 and paginas < 2000:
                paginas = paginas-(paginas*0.20)
                return int(paginas)
            elif paginas >= 2000 and paginas < 20000:
                paginas = paginas-(paginas*0.25)
                return int(paginas)
            elif paginas >= 20000:
                print("Você ultrapassou o limite de páginas, tente novamente.")
                print(" ")
                continue
        except ValueError:  
            print("Entrada inválida, tente novamente.")
            print(" ")
            continue

def servico_extra():
    while True:
        print(" ")
        adicional = input("Escolha o adicional desejado: " \
        "\n1 - Encadernação simples (R$ 15,00)" \
        "\n2 - Encadernação de capa dura (R$ 40,00)" \
        "\n0 - Nenhum adicional (R$ 0,00) ")
        if adicional == "1":
            return 15
        elif adicional == "2":
            return 40
        elif adicional == "0":
            return 0
        else:
            print("Adicional inválido, tente novamente.")
            continue        

print("--------------------------------------------")
print("Seja bem vindo à copiadora Braian Vargas!!!")
print("--------------------------------------------")
servico = escolha_servico()
paginas_com_desconto = num_paginas() # aqui eu chamo a função que valida o número de páginas e aplica o desconto se necessário para essa variavel
extra = servico_extra()

valor_total = (servico * paginas_com_desconto) + extra # aqui eu calculo o valor total, tudo na main
print(" ")
print(f"---------------- Total de: R$ {valor_total:.2f} --------------")
print(f"(Serviço: R$ {servico:.2f} * Páginas: {paginas_com_desconto:.0f} + Adicional: R$ {extra:.2f})") # aqui eu mostro o valor total, com o valor do serviço, páginas e adicional
print(" ")
print("Obrigado por usar nossos serviços, volte sempre!!!!")
print(" ")