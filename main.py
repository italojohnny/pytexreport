#!/usr/python3.5

class pytex_report (object):
    def __init__ (self):
        pass
    def __del__ (self):
        pass
    def testando (self):
        dados = [{'nome':'italo', 'sobrenome':'johnny', 'nascimento': '23/03/1989', 'profissao':'programador', 'endereco':'rua dos bobos', 'bairro': 'jardim luiza', 'cidade':'franca', 'estado':'sao paulo'}]

        cabecalho = r'''
        \begin{longtable}{
        p{.1\textwidth}
        p{.1\textwidth}
        p{.1\textwidth}
        p{.1\textwidth}
        p{.1\textwidth}
        p{.1\textwidth}
        p{.1\textwidth}
        p{.1\textwidth}
        p{.1\textwidth}
        }
        '''
        rodape = r'''
        \end{longtable}
        '''
        print(cabecalho)
        print("%s & %s & %s & %s & %s & %s & %s & %s \\\\ \\hline" % ('nome', 'sobrenome', 'nascimento', 'profissao', 'endereco', 'bairro', 'cidade', 'estado'))
        print(r"\endhead")
        for j in range(0, 300):
            for i in dados:
                print("%s & %s & %s & %s & %s & %s & %s & %s \\\\ \\hline" % (i['nome'], i['sobrenome'], i['nascimento'], i['profissao'], i['endereco'], i['bairro'], i['cidade'], i['estado']))
        print(rodape)


def main ():
    pytex_report().testando()

if __name__ == "__main__": main()
#python main.py > tmp.tex && make
