from classes import Usuario

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def entrada_para_centavos(valor):
    if valor[0] == '-':
        raise ValueError("Valor negativo")

    #check if the value is separeted by a comma
    if ',' in valor:
        return int(valor.split(',')[0])*100 + int(valor.split(',')[1])
    if '.' in valor:
        return int(valor.split('.')[0])*100 + int(valor.split('.')[1])
    else:
        return int(valor)*100
    
if __name__ == '__main__':
    user = Usuario(0)

    while True:
        opcao = input(menu)

        if opcao == 'd':
            valor = entrada_para_centavos(input("Digite o valor do depósito: "))
            #Opta-se por utilizar valores em centavos como inteiro ao invés de lidar com float por possíveis perda de valores em arredondamento
            user.depositar(valor)
        
        elif opcao == 's':
            valor = entrada_para_centavos(input("Digite o valor do saque: "))
            user.sacar(valor)
        
        elif opcao == 'e':
            print(user.extrato)
            #also showing the balance right now
            print(f"Saldo atual: R${user.saldo/100:.2f}")
        
        elif opcao == 'q':
            break

        else:
            print("Opção inválida")





