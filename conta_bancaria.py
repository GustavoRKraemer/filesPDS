class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def deposita(self, valor):
        self.saldo += valor
    def exibirDetalhes(self):
        print("Numero da Conta:", self.numero)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)
    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")
#estou criando uma instancia do objeto ContaBancaria
#com o nome de conta_do_gustavo
conta_do_gustavo = ContaBancaria("1234-5", "Gustavo", 100)

conta_do_gustavo.depositar(10000000)
conta_do_gustavo.sacar(200)
conta_do_gustavo.exibirDetalhes()