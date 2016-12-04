#!/usr/python3.5
import re
from modules import interfaceDB

class pytex_report (object):
    def __init__ (self, sql):
        self.resultado = interfaceDB.easyDBInterface(sql)
        self.tamanho = 0
        self.tabela = "no results"
        if self.resultado:
            self.tamanho = len(self.resultado['keys'])

        if self.tamanho > 0:
            self.iterador = self.iterador_registro()
            self.tabela = self.relatorio()

    def iterador_registro (self):
        texto = "%s"
        for i in range(self.tamanho -1):
            texto += " & %s"
        texto += r" \\ \hline"
        return texto

    def trata_texto_tex (self, texto):
        return re.sub(r"(_|$)", r"\\\1", texto) # adicionar outras excessoes

    def relatorio (self):
        tabela = r"\begin{longtable}{ *%s{p{0.2\textwidth}} }" % self.tamanho

        tabela+="\n"
        tabela+= self.iterador % tuple([self.trata_texto_tex(x) for x in self.resultado['keys']])
        tabela+="\n\\endhead"

        for i in self.resultado['values']:
            tabela+="\n"
            tabela+= self.iterador % tuple([self.trata_texto_tex(str(i[x])) for x in self.resultado['keys']])

        tabela+= "\n"
        tabela+= r"\end{longtable}"
        return tabela

def main ():
    print(pytex_report("select * from actor").tabela)

if __name__ == "__main__": main()

#http://tex.stackexchange.com/questions/42606/overfull-warning-when-using-longtable
