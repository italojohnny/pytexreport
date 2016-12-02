#!/usr/python3.5
import psycopg2
import psycopg2.extras

class pytex_report (object):
    def __init__ (self, banco='', usuario='', senha='', ip='192.168.100.253', porta='5432'):
        self.conexao = psycopg2.connect(database=banco, user=usuario, password=senha, host=ip, port=porta)

    def __del__ (self):
        self.conexao.close()

    def exec_query (self, query):
        cursor = self.conexao.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        return cursor.fetchall()

def main ():
    results = pytex_report().exec_query("select * from f_bilhetes_chamadas order by horario desc limit 100")
    print(r"\begin{longtable}{ *4{p{0.24\textwidth}} }")

    print(r"\multicolumn{4}{c}{Relatorio}\\ \hline")
    print(r"%s & %s & %s & %s \\ \hline" % ('origem', 'destino', 'horario', 'status'))
    print(r"\endfirsthead")
    print(r"\hline")

    print(r"%s & %s & %s & %s \\ \hline" % ('origem', 'destino', 'horario', 'status'))
    print(r"\endhead")
    print(r"\hline")

    for i in results:
        print(r"%s & %s & %s & %s \\ \hline" % (i['origem'], i['destino'], i['horario'], i['status']))

    #print(r"\hline")
    #print(r"\multicolumn{4}{c}{Relatorio}\\ \hline")
    #print(r"\endfoot")
    print(r"\hline")

    print(r"\endlastfoot")
    print(r"\multicolumn{4}{c}{Relatorio}\\")

    print(r"\end{longtable}")

if __name__ == "__main__": main()

#http://tex.stackexchange.com/questions/42606/overfull-warning-when-using-longtable
