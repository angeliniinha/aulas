class Funcionario:
    def _init_(self, nome, matricula, salario_fixo):
        self.__nome = nome
        self.__matricula = matricula
        self.salario_fixo = salario_fixo

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @property
    def salario_fixo(self):
        return self.__salario_fixo

    @salario_fixo.setter
    def salario_fixo(self, valor):
        if valor >= 0:
            self.__salario_fixo = valor
        else:
            print("Erro: salário não pode ser negativo.")
            self.__salario_fixo = 0

    def calcular_salario(self):
        pass

    def exibir(self):
        print(
            f"Nome: {self.nome} | "
            f"Matrícula: {self.matricula} | "
            f"Tipo: {self._class.name_} | "
            f"Salário: R$ {self.calcular_salario():.2f}"
        )


class CLT(Funcionario):
    def _init_(self, nome, matricula, salario_fixo):
        super()._init_(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.salario_fixo


class Vendedor(Funcionario):
    def _init_(self, nome, matricula, salario_fixo, total_vendas):
        super()._init_(nome, matricula, salario_fixo)
        self.__total_vendas = total_vendas

    @property
    def total_vendas(self):
        return self.__total_vendas

    @total_vendas.setter
    def total_vendas(self, valor):
        if valor >= 0:
            self.__total_vendas = valor
        else:
            print("Erro: vendas não podem ser negativas.")
            self.__total_vendas = 0

    def calcular_salario(self):
        return self.salario_fixo + (self.total_vendas * 0.10)


class Gerente(Funcionario):
    def _init_(self, nome, matricula, salario_fixo):
        super()._init_(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.salario_fixo + 1500


funcionarios = [
    CLT("Ana", "001", 3000),
    Vendedor("Bruno", "002", 2000, 12000),
    Gerente("Carla", "003", 5000)
]

for funcionario in funcionarios:
    funcionario.exibir()
