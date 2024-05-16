LIMITE_SAQUE = 3

class Usuario:
    def __init__(self,saldo):
        self.saldo = saldo
        self.limite = 50000 #adaptado para centavos, original era 500 reais que é 50 mil centavos
        self.num_saque = 0
        self.extrato = ""

    
    def depositar(self,valor):
        self.saldo += valor
        #adicionando ao extrato
        self.extrato += f"Depósito de R${valor/100:.2f}\n"
    

    def sacar(self,valor):
        qtt_saque = self.num_saque < LIMITE_SAQUE
        valor_valido = (self.saldo >= valor) and (valor <= self.limite)

        if qtt_saque and valor_valido:
            self.saldo -= valor
            self.num_saque += 1
            #adicionando ao extrato
            self.extrato += f"Saque de R${valor/100:.2f}\n"
        
        else:
            print("Saldo insuficiente")