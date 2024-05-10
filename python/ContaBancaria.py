class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0
        self.limite = 500

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, *, valor):
        if self.saques_diarios < 3:
            if 0 < valor <= self.limite and valor <= self.saldo:
                self.saldo -= valor
                self.saques.append(valor)
                self.saques_diarios += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            elif valor > self.limite:
                print(f'O valor máximo por saque é de R$ {self.limite:.2f}.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('Você atingiu o limite diário de saques.')

    def extrato(self):
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
            return

        print('Extrato:')
        print('Depósitos:')
        for deposito in self.depositos:
            print(f'Depósito: R$ {deposito:.2f}')
        print('Saques:')
        for saque in self.saques:
            print(f'Saque: R$ {saque:.2f}')

        print(f'Saldo atual: R$ {self.saldo:.2f}')
