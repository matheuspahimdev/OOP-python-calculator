# Cria a classe que será importada no arquivo main.py e que realizará as contas
class Operations:

    # Método inicializador da classe para deixar explícito os valores internos no "self"
    def __init__(self, num1, op, num2) -> None:
        self.num1 = num1
        self.op = op
        self.num2 = num2

    # Métodos para a realização das operações
    def soma(self) -> float:
        return self.num1 + self.num2

    def subt(self) -> float:
        return self.num1 - self.num2

    def mult(self) -> float:
        return self.num1 * self.num2

    def divs(self) -> float:
        return self.num1 / self.num2
    
    # Execução das contas
    def operation(self) -> str:

        # Decide qual conta realizar com base no sinal do operador
        match (self.op):

            # Se o operador é "+" executa o seguinte bloco de código:
            case "+":

                # Checa se o valor retornado pelo método "self.soma()" é inteiro
                if self.soma().is_integer():
                    # Se for inteiro retorna um valor sem virgula
                    return f"O resultado é: {self.soma():.0f}"
                
                else:
                    # Se não for inteiro retorna um valor com dois números depois da virgula
                    return f"O resultado é: {self.soma():.2f}"

            # Se o operador é "-" executa o seguinte bloco de código:
            case "-":

                # Checa se o valor retornado pelo método "self.subt()" é inteiro
                if self.subt().is_integer():
                    # Se for inteiro retorna um valor sem virgula
                    return f"O resultado é: {self.subt():.0f}"
                
                else:
                    # Se não for inteiro retorna um valor com dois números depois da virgula
                    return f"O resultado é: {self.subt():.2f}"

            # Se o operador é "*" executa o seguinte bloco de código:
            case "*":

                # Checa se o valor retornado pelo método "self.mult()" é inteiro
                if self.mult().is_integer():
                    # Se for inteiro retorna um valor sem virgula
                    return f"O resultado é: {self.mult():.0f}"
                
                else:
                    # Se não for inteiro retorna um valor com dois números depois da virgula
                    return f"O resultado é: {self.mult():.2f}"

            # Se o operador é "/" executa o seguinte bloco de código:
            case "/":

                # Testa para ver se o divisor retornaria o erro "ZeroDivisionError"
                try:
                    # Se o valor de self.num2 for zero essa linha de código executa o bloco "except"
                    2 / self.num2

                # Executa caso o número for zero
                except:
                    # Finaliza o código e Retorna a mengasem "Impossível dividir por zero"
                    raise Exception("Impossível dividir por zero")

                # Se não retornar erro executa o bloco de código "else" normalmente
                else:

                    # Checa se o valor retornado pelo método "self.divs()" é inteiro
                    if self.divs().is_integer():
                        # Se for inteiro retorna um valor sem virgula
                        return f"O resultado é: {self.divs():.0f}"
                    
                    else:
                        # Se não for inteiro retorna um valor com dois números depois da virgula
                        return f"O resultado é: {self.divs():.2f}"
