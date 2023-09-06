#classe para validar os inputs
class InputValidator:
    # perguntar e calcular o valor base pelo peso do cachorro
    def cachorro_peso(self):
        while True:
            try:
                weight = int(input('Entre com o peso do cachorro: '))
                if weight >= 50:
                    print('Não aceitamos cachorros tão grandes')
                    print('Por favor entre com o peso do cachorro novamente')
                    continue
                break
            except ValueError:
                print('Você digitou um valor não númerico')
                print('Por favor entre com o peso do cachorro novamente')
        valueBase = 0.0
        if weight < 3:
            valueBase = 40
        if weight >= 3 < 10:
            valueBase = 50
        if weight >= 10 < 30:
            valueBase = 60
        if weight >= 30 < 50:
            valueBase = 70

        return valueBase

    #perguntar e calcular o multiplicador
    def cachorro_pelo(self):
        valid_fur = ['c', 'm', 'l']
        while True:
            fur = input("""Entre com o pelo do cachorro:
c - Pelo Curto
m - Pelo Médio
l - Pelo Longo
>> """)
            if fur not in valid_fur:
                print('Opção inválida')
            else:
                break
        multiplier = 0.0
        if fur == 'c':
            multiplier = 1

        if fur == 'm':
            multiplier = 1.5

        if fur == 'l':
            multiplier = 2

        return multiplier

    # perguntar e calcular o extra
    def cachorro_extra(self):
        extraValue = 0
        while True:
            extra = int(input("""Deseja adicionar mais algum servico?:
1 - Corte de Unhas - R$ 10,00
2 - Escovar Dentes - R$ 12,00
3 - Limpeza de Orelhas - R$ 15,00
0 - Não desejo mais nada
>> """))
            if extra == 1:
                extraValue += 10
            if extra == 2:
                extraValue += 12
            if extra == 3:
                extraValue += 15
            if extra == 0:
                break

        return extraValue


#criação dos objetos
InputValidator = InputValidator()

#chamada dos métodos
valueBase = InputValidator.cachorro_peso()
multiplier = InputValidator.cachorro_pelo()
extra = InputValidator.cachorro_extra()
totalValue = valueBase * multiplier + extra
print(f'Total a pagar(R$): {totalValue} (peso: {valueBase} * pelo: {multiplier} + adicional(is) : {extra})')
