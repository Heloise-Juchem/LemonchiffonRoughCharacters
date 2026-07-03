# EXERCÍCIO 1

# class ContaBancaria:
#     def __init__(self, numero_conta, titular, saldo_inicial=0.0):
#         self.numero_conta = numero_conta
#         self.titular = titular
#         self.saldo = float(saldo_inicial) if saldo_inicial >= 0 else 0.0

#     def depositar(self, valor):
#         if valor > 0:
#             self.saldo += valor
#             print(f"Depósito de R$ {valor:} realizado com sucesso.")
#         else:
#             print("Valor de depósito inválido.")

#     def sacar(self, valor):
#         if valor > 0:
#             if self.saldo >= valor:
#                 self.saldo -= valor
#                 print(f"Saque de R$ {valor:} realizado com sucesso.")
#             else:
#                 print("Saldo insuficiente para realizar o saque.")
#         else:
#             print("Valor de saque inválido.")

#     def consultarSaldo(self):
#         return self.saldo

# conta = ContaBancaria("1234-5", "João Silva", 100.0)
# conta.depositar(50.0)
# conta.sacar(30.0)
# conta.sacar(200.0)
# print(f"Saldo Atual: R$ {conta.consultarSaldo():}")

# EXERCÍCIO 2
# class Funcionario:
#     def __init__(self, nome, cargo, salario):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario = float(salario) if salario >= 0 else 0.0

#     def calcularSalarioAnual(self):
#         return self.salario * 12

#     def aplicarAumento(self, percentual):
#         if percentual >= 0:
#             self.salario += self.salario * (percentual / 100)
#             print(f"Aumento de {percentual}% aplicado. Novo salário: R$ {self.salario:}")
#         else:
#             print("Percentual de aumento não pode ser negativo.")

# func = Funcionario("Maria Souza", "Desenvolvedora", 4000.0)
# print(f"Salário Anual: R$ {func.calcularSalarioAnual():}")
# func.aplicarAumento(10)

# EXERCÍCIO 3
# class Produto:
#     def __init__(self, nome, preco, quantidade_estoque):
#         self.nome = nome
#         self.preco = float(preco) if preco >= 0 else 0.0
#         self.quantidade_estoque = int(quantidade_estoque) if quantidade_estoque >= 0 else 0

#     def atualizarPreco(self, novoPreco):
#         if novoPreco >= 0:
#             self.preco = float(novoPreco)
#         else:
#             print("Preço não pode ser negativo.")

#     def aplicarDesconto(self, percentual):
#         if 0 <= percentual <= 100:
#             self.preco -= self.preco * (percentual / 100)
#         else:
#             print("Percentual de desconto inválido.")

#     def adicionarEstoque(self, quantidade):
#         if quantidade > 0:
#             self.quantidade_estoque += int(quantidade)

#     def removerEstoque(self, quantidade):
#         if quantidade > 0:
#             if self.quantidade_estoque >= quantidade:
#                 self.quantidade_estoque -= int(quantidade)
#             else:
#                 print("Quantidade insuficiente em estoque.")

# prod = Produto("Teclado Mecânico", 150.0, 20)
# prod.aplicarDesconto(10)
# prod.adicionarEstoque(5)
# prod.removerEstoque(10)
# print(f"Produto: {prod.nome} | Preço: R$ {prod.preco:} | Estoque: {prod.quantidade_estoque}")

# EXERCÍCIO 4
# class ConsultaMedica:
#   def __init__(self, data, hora, paciente):
#       self.data = data
#       self.hora = hora
#       self.paciente = paciente
#       self.status = "Agendada"

#   def cancelar(self):
#       if self.status != "Cancelada":
#           self.status = "Cancelada"
#           print(f"Consulta do paciente {self.paciente} foi CANCELADA com sucesso.")
#       else:
#           print("Esta consulta já está cancelada.")

#   def reagendar(self, nova_data, nova_hora):
#       if self.status == "Cancelada":
#           print("Não é possível reagendar uma consulta que foi cancelada. Crie um novo agendamento.")
#       else:
#           if self.data == nova_data and self.hora == nova_hora:
#               print("A consulta já está agendada para este mesmo dia e horário.")
#           else:
#               self.data = nova_data
#               self.hora = nova_hora
#               self.status = "Agendada"
#               print(f"Consulta reagendada para {self.data} às {self.hora}.")

# consulta = ConsultaMedica("10/11/2026", "14:00", "Carlos Almeida")
# print(f"Status Inicial: {consulta.status}")

# consulta.reagendar("12/11/2026", "15:30")

# consulta.cancelar()
# print(f"Status Final: {consulta.status}")

# EXERCÍCIO 5
# class Fatura:
#   def __init__(self, numero_fatura, valor_original):
#       self.numero_fatura = numero_fatura
#       self.valor_original = float(valor_original) if valor_original >= 0 else 0.0
#       self.valor_final = self.valor_original
#       self.status = "Aberta"

#   def aplicarDesconto(self, percentual):
#       if self.status == "Paga":
#           print("Não é possível aplicar desconto em uma fatura que já foi paga.")
#       elif 0 <= percentual <= 100:
#           desconto = self.valor_original * (percentual / 100)
#           self.valor_final = self.valor_original - desconto
#           print(f"Desconto de {percentual}% aplicado. Novo valor: R$ {self.valor_final:}")
#       else:
#           print("Percentual de desconto inválido. Deve ser entre 0% e 100%.")

#   def marcarPaga(self):
#       if self.status == "Aberta":
#           self.status = "Paga"
#           print(f"Fatura nº {self.numero_fatura} paga com sucesso!")
#       else:
#           print("Esta fatura já foi paga.")

# fatura = Fatura("98765", 500.0)
# fatura.aplicarDesconto(15)  
# fatura.marcarPaga()
# print(f"Fatura: {fatura.numero_fatura} | Status: {fatura.status} | Valor Final: R$ {fatura.valor_final:}")

# EXERCÍCIO 6
# class PedidoVenda:
#   def __init__(self, id_pedido, total_pedido):
#       self.id_pedido = id_pedido
#       self.total_pedido = float(total_pedido) if total_pedido >= 0 else 0.0

#   def calcularTotal(self):
#       return self.total_pedido


# class RelatorioVendas:
#   def gerarTotal(self, lista_pedidos):
#       total_geral = 0.0

#       for pedido in lista_pedidos:
#           total_geral += pedido.calcularTotal()

#       return total_geral

# pedido1 = PedidoVenda("P001", 150.00)
# pedido2 = PedidoVenda("P002", 350.50)
# pedido3 = PedidoVenda("P003", 99.90)

# lista_do_mes = [pedido1, pedido2, pedido3]

# relatorio = RelatorioVendas()
# faturamento_total = relatorio.gerarTotal(lista_do_mes)

# print(f"Faturamento Total do Mês: R$ {faturamento_total:}")

# print(f"Faturamento se a lista estiver vazia: R$ {relatorio.gerarTotal([]):}")
