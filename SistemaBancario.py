class SistemaBancario:
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.conta_logada = None

    def criar_usuario(self):  # Added 'self' as parameter
        cpf = input("Informe o CPF (somente número): ")
        usuario = self.filtrar_usuario(cpf)  # Fixed 'usuarios' to 'self'

        if usuario:
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})  # Fixed 'usuarios' to 'self'

        print("=== Usuário criado com sucesso! ===")

    def filtrar_usuario(self, cpf):  # Added 'self' as parameter
        usuarios_filtrados = [usuario for usuario in self.usuarios if usuario["cpf"] == cpf]  # Fixed 'usuarios' to 'self'
        return usuarios_filtrados[0] if usuarios_filtrados else None

    def logar_conta(self):
        cpf = input("Digite seu cpf: ")
        for conta in self.contas:
            if cpf == conta.usuario["cpf"]:  # Fixed accessing 'cpf' in 'usuario'
                self.conta_logada = conta
                return
        print("Conta não encontrada.")

    def criar_conta(self):
        if self.conta_logada:
            print("Você já está logado.")
            return

        cpf = input("Informe o CPF (somente números): ")
        if any(c.usuario["cpf"] == cpf for c in self.contas):  # Fixed accessing 'cpf' in 'usuario'
            print("Já existe uma conta com este CPF.")
            return

        usuario = self.filtrar_usuario(cpf)
        if not usuario:
            print("Usuário não encontrado.")
            return

        numero_conta = len(self.contas) + 1
        conta = ContaBancaria()
        conta.usuario = usuario
        self.contas.append(conta)
        print(f"Conta criada com sucesso para o CPF {cpf}.")

    def listar_contas(self):
        if not self.contas:
            print("Não há contas cadastradas.")
            return

        print("Lista de contas:")
        for i, conta in enumerate(self.contas, 1):
            print(f"{i}. CPF: {conta.usuario['cpf']}, Saldo: R$ {conta.saldo:.2f}")

    def menu(self):
        menu = """
           ================ MENU ================
           [l]\tLogar
           [d]\tDepositar
           [s]\tSacar
           [e]\tExtrato
           [nc]\tNova conta
           [lc]\tListar contas
           [nu]\tNovo usuário
           [q]\tSair

           => """
        return input(menu)

def main():
    sistema = SistemaBancario()

    while True:
        opcao = sistema.menu()

        if opcao == 'd':
            if not sistema.conta_logada:
                print("Você precisa logar em uma conta primeiro.")
                continue
            valor = float(input("Digite o valor a ser depositado: "))
            sistema.conta_logada.depositar(valor)
        elif opcao == 's':
            if not sistema.conta_logada:
                print("Você precisa logar em uma conta primeiro.")
                continue
            valor = float(input("Digite o valor a ser sacado: "))
            sistema.conta_logada.sacar(valor= valor)
        elif opcao == 'e':
            if not sistema.conta_logada:
                print("Você precisa logar em uma conta primeiro.")
                continue
            sistema.conta_logada.extrato()
        elif opcao == 'nu':
            sistema.criar_usuario()
        elif opcao == "nc":
            sistema.criar_conta()
        elif opcao == "lc":
            sistema.listar_contas()
        elif opcao == 'l':
            sistema.logar_conta()
        elif opcao == 'q':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
