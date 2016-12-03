#!/usr/python3.5
import psycopg2
import psycopg2.extras
import re

class pytex_report (object):
    def __init__ (self, sql):
        self.ip      = '192.168.1.104'
        self.banco   = 'bancodedados'
        self.usuario = 'admteste'
        self.senha   = 'yma2578k'
        self.porta   = '5432'
        self.conexao = psycopg2.connect(database=self.banco, user=self.usuario, password=self.senha, host=self.ip, port=self.porta)

        self.resultado = self.exec_query(sql)
        if self.resultado:
            self.tamanho = len(self.resultado[0])
            self.keys = [x for x in self.resultado[0].keys()]
        else:
            self.tamanho = 0
            self.keys = []
        self.iterador = self.iterador_registro()
        self.tabela = self.relatorio()

    def __del__ (self):
        self.conexao.close()

    def exec_query (self, query):
        cursor = self.conexao.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        return cursor.fetchall()

    def iterador_registro (self):
        texto = "%s"
        for i in range(self.tamanho -1):
            texto += " & %s"
        texto += r" \\ \hline"
        return texto

    def trata_texto_tex (self, texto):
        return re.sub(r"(_)", r"\\\1", texto)

    def relatorio (self):
        tabela = r"\begin{longtable}{ *%s{p{0.24\textwidth}} }" % self.tamanho

        tabela+="\n"
        tabela+= self.iterador % tuple([self.trata_texto_tex(x) for x in self.keys])
        tabela+="\n\\endhead"

        for i in self.resultado:
            tabela+="\n"
            tabela+= self.iterador % tuple([self.trata_texto_tex(str(i[x])) for x in self.keys])

        tabela+= "\n"
        tabela+= r"\end{longtable}"
        return tabela

def main ():
    print(pytex_report("select * from tabela1").tabela)

if __name__ == "__main__": main()

#http://tex.stackexchange.com/questions/42606/overfull-warning-when-using-longtable
