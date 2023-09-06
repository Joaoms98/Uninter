#classe para validar os inputs
class InputValidator:
    # validador do sabor
    def flavorValidator(self, iceCreamFlavor):
        valid_flavors = ['tr', 'pr', 'es']
        if iceCreamFlavor in valid_flavors:
            return True
        else:
            print('Sabor inválido. Tente novamente')
            return False

    # validador da quantidade de bolas de sorvete
    def scoopsValidator(self, scoopsOfIceCream):
        valid_scoops = [1, 2, 3]
        if scoopsOfIceCream in valid_scoops:
            return True
        else:
            print('Número de bolas de sorvete inválido')
            return False

#registro dos preços e sabores
class Menu:
    @property
    def total_Value(self):
        return self._total_Value

    @total_Value.setter
    def total_Value(self, value):
        self._total_Value = value

    # trazer o preço do sorvete
    def setFlavorValue(self, flavor, scoops):
        flavorTr = {1: 6.0, 2: 11.0, 3: 15.0}
        flavorPr = {1: 7.0, 2: 13.0, 3: 18.0}
        flavorEs = {1: 8.0, 2: 15.0, 3: 21.0}

        if flavor == "tr":
            return flavorTr[scoops]
        elif flavor == "pr":
            return flavorPr[scoops]
        elif flavor == "es":
            return flavorEs[scoops]

    # tradutor do código do sabor
    def flavorTranslater(self, iceCreamFlavor):
        flavors = {'tr': 'TRADICIONAL', 'pr': 'PREMIUM', 'es': 'ESPECIAL'}
        return flavors[iceCreamFlavor]

#criação dos objetos
InputValidator = InputValidator()
Menu = Menu()
Menu.total_Value = 0.0

#Apresentação e cardápio
print("""
Bem-vindo a Sorveteria do Joao Victor Menezes de Souza
------------------------------------Cardápio---------------------------------------
| Nº de bolas | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |
|      1      |        R$ 6,00         |       R$ 7,00      |        R$ 8,00      |
|      2      |        R$ 11,00        |       R$ 13,00     |        R$ 15,00     |
|      3      |        R$ 15,00        |       R$ 18,00     |        R$ 21,00     |
-----------------------------------------------------------------------------------
""")

#loop
while True:
    # input para a quantidade de bolas de sorvete e validador
    scoopsOfIceCream = int(input("Entre com o número de bolas de sorvete desejado (1/2/3): "))
    scoopsIsValid = InputValidator.scoopsValidator(scoopsOfIceCream)

    if scoopsIsValid != True:
        continue

    # input para o sabor do sorvete e validador
    iceCreamFlavor = input("Entre com o sabor desejado (tr/pr/es): ")
    flavorIsInvalid = InputValidator.flavorValidator(iceCreamFlavor)

    if flavorIsInvalid != True:
        continue

    # registro de escolha e compra
    totalValue = Menu.setFlavorValue(iceCreamFlavor, scoopsOfIceCream)
    Menu.total_Value += totalValue
    print(f'Você pediu {scoopsOfIceCream} bola de sorvete no sabor {Menu.flavorTranslater(iceCreamFlavor)}: '
          f'R$ {totalValue}')
    # saída do loop
    loop = input("Deseja mais algum sorvete (s/digite outra tecla)?: ")
    if loop != "s":
        break

print(f'O valor total a ser pago: R$ {Menu.total_Value}')