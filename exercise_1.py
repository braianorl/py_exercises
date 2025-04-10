print("Bem-vindo ao Atacado Braian Vargas")

valor_produto = float(input("Digite o valor do produto: ")) #aqui eu defino o valor do produto
quantidade_produto = int(input("Digite a quantidade do produto: ")) #aqui eu defino a quantidade do produto
valor_total_sem_desconto = valor_produto * quantidade_produto #aqui eu defino o valor total do carrinho

if valor_total_sem_desconto < 2500:
    print(f"Valor total: R$ {valor_total_sem_desconto:.2f}")
    print(f"Esse valor não recebe desconto")

elif valor_total_sem_desconto >= 2500 and valor_total_sem_desconto < 6000:
        valor_total_com_desconto = valor_total_sem_desconto - (valor_total_sem_desconto * 0.04)
        print(f"Valor total SEM desconto: R$ {valor_total_sem_desconto:.2f}")
        print(f"Valor total COM desconto de 4%: R$ {valor_total_com_desconto:.2f}")

elif valor_total_sem_desconto >= 6000 and valor_total_sem_desconto < 10000:
        valor_total_com_desconto = valor_total_sem_desconto - (valor_total_sem_desconto * 0.07)
        print(f"Valor total SEM desconto: R$ {valor_total_sem_desconto:.2f}")
        print(f"Valor total COM desconto de 7%: R$ {valor_total_com_desconto:.2f}")

else:
    if valor_total_sem_desconto >= 10000:
        valor_total_com_desconto = valor_total_sem_desconto - (valor_total_sem_desconto * 0.11)
        print(f"Valor total SEM desconto: R$ {valor_total_sem_desconto:.2f}")
        print(f"Valor total COM desconto de 11%: R$ {valor_total_com_desconto:.2f}")

print("Obrigado por comprar no Atacado Braian Vargas, volte sempre!!!!")