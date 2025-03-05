print('Controle de finanças pessoais')
opcao = ['supermercado', 'farmacia', 'lanches', 'roupas', 'calcados', 'casa']
total_gasto = 0


def menu_opcao():
    print('CADASTRAR DESPESA [1] | RELATÓRIO DE DESPESA [2] | SAIR [3]')
    menu = input('Digite a opção: ')
    return menu


def obter_opcao():
    print('Supermercado | Farmácia | Lanches | Roupas | Calçados | Casa')
    print('** Digite uma das opções acima **')
    tipo_de_gasto = input('Qual tipo do gasto: ').lower().strip()
    valor_gasto = float(input('Digite o valor R$: ').isdigit())
    return tipo_de_gasto, valor_gasto


while True:
    opcao_menu = menu_opcao()
    if opcao_menu == '1':
        tipo_de_gasto, valor_gasto = obter_opcao()
        total_gasto += valor_gasto
        print('Despesa cadastrada com sucesso!')
    elif opcao_menu == '2':
        print('Relatório de despesas')
        print('Total gasto: R$', total_gasto)
    elif opcao_menu == '3':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente!')
