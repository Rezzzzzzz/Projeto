import pdb
import sys
import os.path
from distutils.dir_util import copy_tree
import time
import getopt




def copia(original, destinal):
    copy_tree(original, destinal)  # Copia ficheiros da origem para o destino


def s(original, destinal):
    dir_nome = os.path.abspath(original)
    dir_nome2 = os.path.abspath(destinal)

    if os.path.isdir(dir_nome):
        a = sum([len(files) for r, d, files in os.walk(dir_nome)])
        b = sum([len(files) for r, d, files in os.walk(dir_nome2)])
        print("Número de ficheiros na origem: " + str(a) + ", Número de ficheiros alterados: " + str(b))
        print("Last modified: %s" % time.ctime(os.path.getmtime(dir_nome)))

    elif not os.path.isdir(dir_nome):
        print("A diretoria " + dir_nome + " não existe no seu computador. :(")
        sys.exit(2)

    elif not os.path.isdir(dir_nome):
        try:
            os.mkdir(dir_nome2)

        except OSError:
            print("O diretorio" + dir_nome2 + " não foi criado com sucesso! :(")
            sys.exit(2)

        else:
            print("O diretorio " + dir_nome2 + " foi criado com sucesso! :)")


def h():
    print("""
          -------- Comandos Disponíveis-------- 

          -s :  Indica o numero de ficheiros na origem e o número de ficheiros alterados.
          -v : Informação detalhada sobre o ficheiro da origem e se foi ou não transferido e ainda uma lista dos ficheiros que \n             apenas existem no destino
          -d : Debug.
          --origem: Introduzir a Origem.
          --destino: Introduzir o Destino.
          """)


original = r"Origem"
destinal = r"Destino"

CMD_argumentos = sys.argv

Lista_argumentos = CMD_argumentos[1:]


try:
    argumentos, valores = getopt.getopt(Lista_argumentos, 'vhds',
                                        ["origem=", "destino="])
except getopt.error as err:
    print("Erro no argumento usado.")
    sys.exit(2)

for argumento, valor in argumentos:

    if argumento in "-s":
        s(original, destinal)

    elif argumento in "-h":
        h()

    elif argumento in "-d":
        pdb.set_trace()
        # Debug

    elif argumento in "-v":
        pass
        # Dar informação detalhada sobre os ficheiros

    elif argumento in "--origem":
        original = valor

    elif argumento in "--destino":
        destinal = valor

    # TODO Percorrer todos os ficheiros da diretoria






