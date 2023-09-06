#classe que contem os métodos para o crud do colaborador
class Colaborador:

    #método para cadastrar
    def cadastrar_colaborador(self,id):
        print(f'id do colaborador: {id}')
        nome = input('por favor entre com o nome:')
        setor = input('por favor entre com o setor:')
        pagamento = int(input('por favor entre com o pagamento (R$):'))

        colaborador = {'id': id, 'nome': nome, 'setor': setor, 'pagamento': pagamento}
        lista_colaboradores.append(colaborador)

    #método para consultar
    def consultar_colaborador(self):
        try:
            opcao = int(input(
                """Escolha a opção desejada:
1-Consultar Todos
2-Consultar por id
3-Consultar por setor
4-Retornar
>>>"""))

            if opcao == 1:
                for colaborador in lista_colaboradores:
                    print(
                        f"""---------------------------------------
Id : {colaborador['id']}  
Nome: {colaborador['nome']}  
Setor: "{colaborador['setor']} 
Pagamento: {colaborador['pagamento']}""")
            elif opcao == 2:
                id = int(input('Digite o id do colaborador: '))
                for colaborador in lista_colaboradores:
                    if colaborador['id'] == id:
                        print(
                            f"""---------------------------------------
Id : {colaborador['id']}  
Nome: {colaborador['nome']}  
Setor: "{colaborador['setor']} 
Pagamento: {colaborador['pagamento']}""")
            elif opcao == 3:
                setor = input('Digite o setor do(s) colaborador(es): ')
                for colaborador in lista_colaboradores:
                    if colaborador['setor'] == setor:
                        print(
                            f"""---------------------------------------
Id : {colaborador['id']}  
Nome: {colaborador['nome']}  
Setor: "{colaborador['setor']} 
Pagamento: {colaborador['pagamento']}""")
            elif opcao == 4:
                return
        except ValueError:
            print('Opção Inválida')

    #método para remover
    def remover_colaborador(self):
        id = int(input('Digite o Id do colaborador a ser removido: '))
        for colaborador in lista_colaboradores:
            if colaborador['id'] == id:
                lista_colaboradores.remove(colaborador)


#criação do objeto e set das variáveis
Colaborador = Colaborador()
id_global = 0
lista_colaboradores = list()

#loop
while True:
    try:
        opcao = int(input(
            """Bem-vindo ao Controle de Colaboradores do Joao Victor Menezes De Souza
***************************************************
-------------------Menu Principal------------------
Escolha a opção desejada:
1-Cadastrar Colaborador
2-Consultar Colaborador(es)
3-Remover Colaborador
4-Sair
>>>"""))

        #condicional para chamar o método específico do crud
        if opcao == 1:
            id_global += 1
            Colaborador.cadastrar_colaborador(id_global)
        elif opcao == 2:
            Colaborador.consultar_colaborador()
        elif opcao == 3:
            Colaborador.remover_colaborador()
        elif opcao == 4:
            break
    except ValueError:
        print('Opção Inválida')
