# Importa a classe e seus métodos da pasta modules do arquivo operations.py
# Todos os métodos do arquivo serão executados com o préfixo "operate."
import modules.operations as operate

# Main loop
while True:

    # Executa o processo principal da calculadora
    print("+===================+")
    print("+    CALCULADORA    +")
    print("+===================+")

    # Cria uma lista contendo cada parte do input
    # número1 / operador / número 2
    listaOperacao = input("Insira a operação: ").split()

    # Checa se há mais de três itens na lista
    if len(listaOperacao) > 3:
        raise Exception("Valores Adicionais")

    # Checa para inputs inválidos como strings em vez de números
    try:
        # Tenta transformar os números em float, se forem string retornam erro e executa o execept
        listaOperacao[0] = float(listaOperacao[0])
        listaOperacao[2] = float(listaOperacao[2])

    # O bloco de código só executa se o bloco try retorna erro
    except:
        # Finaliza o código e Retorna a mengasem "Valores Inválidos"
        raise Exception("Valores Inválidos")

    # Cria uma nova instância da classe Operations
    objOperacao = operate.Operations(listaOperacao[0], listaOperacao[1], listaOperacao[2])

    # Dá output do resultado após a execução do método de operação do objeto da classe do outro arquivo
    print(objOperacao.operation())
