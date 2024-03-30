class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if self.saques_diarios < 3:
            if valor <= 500 and valor <= self.saldo:
                self.saldo -= valor
                self.saques.append(valor)
                self.saques_diarios += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            elif valor > 500:
                print('O valor máximo por saque é de R$ 500.00.')
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


def main():
    conta = ContaBancaria()

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu).lower()

        if opcao == 'd':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == 's':
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == 'e':
            conta.extrato()
        elif opcao == 'q':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
