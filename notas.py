
# fazer supostamente a soma de notas dada como aprovado, recuperação ou reprovado.!!!

# aqui seria dentro de outra arquivo pra poder usar a funcoes !!!

# from notas import aluno

#aqui chamar as funcoes !!! 
 
#a2 = aluno("eduardo")
#a2.soma()


class aluno:
    def __init__(self, nome):
        self.nome = nome
        self.nota = None


    def soma(self):
        print('\n=== somar notas ===\n')
        while True:
            try:
                soma = float(input('digitar sua nota: '))
                if soma < 0 or soma > 10:
                    print('a nota deve estar entre 0 a 10! ')
                    continue

                self.nota = soma

                if self.nota >= 7: 
                    print(f'sua nota {self.nome} e {self.nota} voce esta aprovado!')
                    break
                elif self.nota <= 4.99:
                    print(f'sua nota {self.nome} e {self.nota} voce esta de recuperacao !')
                    break
                else:
                    print(f'sua nota {self.nome} e {self.nota} voce foi reprovado !')
                    break
            except ValueError:
                print('apenas numeros! ')

       