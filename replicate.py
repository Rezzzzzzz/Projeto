"""Imports necessários"""

import sys
import os.path
import time
import getopt
import shutil
from distutils.dir_util import copy_tree


def debug(origin, destiny):
    """Mostra o que o código faz mas sem alterar nada"""

    origin_path = os.path.abspath(origin)  # Path da Origem
    origin_list = os.listdir(origin)  # Lista com os ficheiros da Origem
    destiny_path = os.path.abspath(destiny)  # Path do Destino
    destiny_list = os.listdir(destiny)  # Lista com os ficheiros do Destino
    exist_list = []

    for i in range(0, len(origin_list)):  # Percorre os ficheiros da Origem
        origin_path_join = os.path.join(origin_path, origin_list[i])
        origin_raw_string = r"{}".format(origin_list[i])

        for len_destiny_list in range(
                0, len(destiny_list)):  # Percorre os ficheiros do destino
            destiny_path_join = os.path.join(destiny_path,
                                             destiny_list[len_destiny_list])
            destiny_raw_string = r"{}".format(destiny_list[len_destiny_list])
            destiny_path_join_exist = os.path.join(destiny_path,
                                                   origin_list[i])

            if destiny_raw_string == origin_raw_string:

                if time.ctime(
                        os.path.getmtime(origin_path_join)) != time.ctime(
                            os.path.getmtime(destiny_path_join)):
                    print("O ficheiro ou diretorio " + str(origin_list[i]) +
                          " iria ser copiado para o diretório Destino.")

                elif time.ctime(
                        os.path.getmtime(origin_path_join)) == time.ctime(
                            os.path.getmtime(destiny_path_join)):
                    print("O ficheiro ou diretorio " + str(origin_list[i]) +
                          " não iria ser copiado para o diretório Destino.")

            if not os.path.exists(destiny_path_join_exist):
                exist_list.append(str(origin_list[i]))

    without_duplicates_debug = list(set(exist_list))  # Retira os duplicados

    if without_duplicates_debug:
        for file_debug in without_duplicates_debug:
            print("O ficheiro " + str(file_debug) +
                  " iria ser copiado para o diretório Destino.")


def copy(src, destiny, src_destiny):
    """Copia diretórios e ficheiros para o destino"""

    if os.path.isdir(src) and not os.path.exists(src_destiny):
        shutil.copytree(src, src_destiny)

    elif os.path.isfile(src):
        shutil.copy2(src, destiny)


def silence_information(origin):
    """Mostra os números de ficheiros na origem e ficheiros modificados"""

    copy_tree(origin, DESTINY)
    dir_name_origin = os.path.abspath(origin)

    if os.path.isdir(dir_name_origin):
        sum_origin = sum(
            [len(files) for r, d, files in os.walk(dir_name_origin)])
        print("\nNúmero de ficheiros na origem: " + str(sum_origin) + "." +
              " \nNúmero de ficheiros modificados: " + str(sum_origin) + ".")


def help():
    """Comando Help mostra a função de todos os comandos"""
    print("""
          -------- Comandos Disponíveis-------- 

          -s : Indica o numero de ficheiros na origem e o número de ficheiros alterados.
          -v : Informação detalhada sobre o ficheiro da origem.
          -d : Debug.
          --origem: Introduzir a Origem.
          --destino: Introduzir o Destino.
          """)


def detailed_information(origin, destiny):
    """Informação detalhada sobre a Origem e o Destino"""

    copy_tree(origin, destiny)  # Copia os ficheiros da origem para o destino
    origin_path = os.path.abspath(origin)  # Path da origem
    origin_list = os.listdir(origin)  # Lista com ficheiros da origem
    destiny_path = os.path.abspath(destiny)  # Path do destino
    destiny_list = os.listdir(destiny)  # Lista com ficheiros do destino

    print("")
    print("----------------------ORIGEM----------------------")
    print("")

    for file_name in origin_list:
        join_paths = os.path.join(origin_path, file_name)

        print("Nome do ficheiro: %s" % file_name)
        print("Tamanho do ficheiro em bytes: %s" % os.path.getsize(join_paths))
        print("Última vez que foi modificado: %s" %
              time.ctime(os.path.getmtime(join_paths)))
        print("Última vez que foi acessado: %s" %
              time.ctime(os.path.getatime(join_paths)))
        print("Data de criação: %s" % time.ctime(os.path.getctime(join_paths)))
        print("")

    print("----------------------DESTINO----------------------")
    print("")

    for file_name in destiny_list:
        join_paths = os.path.join(destiny_path, file_name)

        print("Nome do ficheiro: %s" % file_name)
        print("Tamanho do ficheiro: %s" % os.path.getsize(join_paths))
        print("Última vez que foi modificado: %s" %
              time.ctime(os.path.getmtime(join_paths)))
        print("Última vez que foi acessado: %s" %
              time.ctime(os.path.getatime(join_paths)))
        print("Data de criação: %s" % time.ctime(os.path.getctime(join_paths)))
        print("")

    print("Lista de todos os ficheiros na Origem: " + str(origin_list))

    # Dar informação detalhada sobre os ficheiros.


if __name__ == "__main__":

    LIST_EXIST_MAIN = []
    ORIGIN = "Origem"
    DESTINY = "Destino"

    TERMINAL_ARGUMENTS = sys.argv
    ARGUMENTS_LIST = TERMINAL_ARGUMENTS[1:]

    try:
        ARGUMENTS, VALUES = getopt.getopt(ARGUMENTS_LIST, 'vhds',
                                          ["origem=", "destino="])
    except getopt.error as err:
        print("Erro no argumento usado consulte o help: ")
        help()
        sys.exit(2)

    if not ARGUMENTS_LIST:

        if not os.path.isdir(ORIGIN):
            print("\nO diretorio " + ORIGIN +
                  " não existe no seu computador. :(\n")
            sys.exit(2)

        elif not os.path.isdir(DESTINY):
            try:
                os.mkdir(DESTINY)

            except OSError as error:
                print("\nO diretorio" + DESTINY +
                      " não foi criado com sucesso! :(\n")
                print(error)
                sys.exit(2)

            else:
                print("\nO diretorio " + DESTINY +
                      " foi criado com sucesso! :)\n")

        DIR_ORIGIN = os.path.abspath(ORIGIN)  # Path da origem
        DIR_DESTINY = os.path.abspath(DESTINY)  # Path do destino
        ORIGIN_LIST_MAIN = os.listdir(ORIGIN)  # Lista com ficheiros da origem
        DESTINY_LIST_MAIN = os.listdir(
            DESTINY)  # Lista com ficheiros do destino
        LIST_EXIST_MAIN = []  # Lista usada para retirar os duplicates

        for len_origin in range(0, len(ORIGIN_LIST_MAIN)):
            origin_path_join_main = os.path.join(DIR_ORIGIN,
                                                 ORIGIN_LIST_MAIN[len_origin])
            origin_raw_string_main = r"{}".format(ORIGIN_LIST_MAIN[len_origin])

            for len_destiny in range(0, len(DESTINY_LIST_MAIN)):
                destiny_path_join_main = os.path.join(
                    DIR_DESTINY, DESTINY_LIST_MAIN[len_destiny])
                destiny_raw_string_main = r"{}".format(
                    DESTINY_LIST_MAIN[len_destiny])
                destiny_path_join_exist_main = os.path.join(
                    DIR_DESTINY, ORIGIN_LIST_MAIN[len_origin])

                if destiny_raw_string_main == origin_raw_string_main:
                    print("O ficheiro ou diretorio " +
                          str(ORIGIN_LIST_MAIN[len_origin]) +
                          " existe no Destino.")

                    if time.ctime(os.path.getmtime(
                            origin_path_join_main)) > time.ctime(
                                os.path.getmtime(destiny_path_join_main)):
                        LIST_EXIST_MAIN.append(
                            str(ORIGIN_LIST_MAIN[len_origin]))

                elif not os.path.exists(destiny_path_join_exist_main):
                    LIST_EXIST_MAIN.append(str(ORIGIN_LIST_MAIN[len_origin]))

        WITHOUT_DUPLICATES = list(set(LIST_EXIST_MAIN))

        if WITHOUT_DUPLICATES:
            for file in WITHOUT_DUPLICATES:
                src_file = os.path.join(
                    DIR_ORIGIN,
                    file)  # Faz um join do path da Origem com o do ficheiro
                src_file_destiny = os.path.join(DIR_DESTINY, file)
                copy(src_file, DIR_DESTINY, src_file_destiny)

            print("\nCópia concluída com sucesso! :)")

    for argument, value in ARGUMENTS:

        if argument in "-s":
            silence_information(ORIGIN)

        elif argument in "-h":
            help()

        elif argument in "-d":
            debug(ORIGIN, DESTINY)

        elif argument in "-v":
            detailed_information(ORIGIN, DESTINY)

        elif argument in "--origem":
            ORIGIN = value

        elif argument in "--destino":
            DESTINY = value
