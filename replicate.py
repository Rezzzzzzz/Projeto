import sys
import os.path
import time
import getopt
import shutil
from distutils.dir_util import copy_tree


def debug(origin, destiny):

    origin_path = os.path.abspath(origin)  # Path da Origem
    origin_list = os.listdir(origin)  # Lista com os ficheiros da Origem
    destiny_path = os.path.abspath(destiny)  # Path do Destino
    destiny_list = os.listdir(destiny)  # Lista com os ficheiros do Destino
    exist_list = []

    for i in range(0, len(origin_list)):  # Percorre os ficheiros da Origem
        origin_path_join = os.path.join(origin_path, origin_list[i])
        origin_raw_string = r"{}".format(origin_list[i])

        for c in range(0, len(destiny_list)):  # Percorre os ficheiros do destino
            destiny_path_join = os.path.join(destiny_path, destiny_list[c])
            destiny_raw_string = r"{}".format(destiny_list[c])
            destiny_path_join_exist = os.path.join(destiny_path, origin_list[i])

            if destiny_raw_string == origin_raw_string:

                if time.ctime(os.path.getmtime(origin_path_join)) != time.ctime(os.path.getmtime(destiny_path_join)):
                    print("O ficheiro ou diretorio " + str(origin_list[i]) + " iria ser copiado para o diretório Destino.")

                elif time.ctime(os.path.getmtime(origin_path_join)) == time.ctime(os.path.getmtime(destiny_path_join)):
                    print("O ficheiro ou diretorio " + str(origin_list[i]) + " não iria ser copiado para o diretório Destino.")

            if not os.path.exists(destiny_path_join_exist):
                exist_list.append(str(origin_list[i]))

    without_duplicates_debug = list(set(exist_list))  # Retira os duplicados

    if without_duplicates_debug:
        for file_debug in without_duplicates_debug:
            print("O ficheiro " + str(file_debug) + " iria ser copiado para o diretório Destino.")


def copy(src, destiny, src_destiny):  #TODO o de diretórios ainda não está a funcionar

    if os.path.isdir(src) and not os.path.exists(src_destiny):
        shutil.copytree(src, src_destiny)

    elif os.path.isfile(src):
        shutil.copy2(src, destiny)


def silence_information(origin):

    copy_tree(origin,destiny)
    dir_name_origin = os.path.abspath(origin)

    if os.path.isdir(dir_name_origin):
        sum_origin = sum([len(files) for r, d, files in os.walk(dir_name_origin)])
        print("\nNúmero de ficheiros na origem: " + str(sum_origin) + "." + " \nNúmero de ficheiros modificados: " + str(sum_origin) + ".")


def help():
    print("""
          -------- Comandos Disponíveis-------- 

          -s : Indica o numero de ficheiros na origem e o número de ficheiros alterados.
          -v : Informação detalhada sobre o ficheiro da origem.
          -d : Debug.
          --origem: Introduzir a Origem.
          --destino: Introduzir o Destino.
          """)


def detailed_information(origin, destiny):

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
        print("Última vez que foi modificado: %s" % time.ctime(os.path.getmtime(join_paths)))
        print("Última vez que foi acessado: %s" % time.ctime(os.path.getatime(join_paths)))
        print("Data de criação: %s" % time.ctime(os.path.getctime(join_paths)))
        print("")

    print("----------------------DESTINO----------------------")
    print("")

    for file_name in destiny_list:

        join_paths = os.path.join(destiny_path, file_name)

        print("Nome do ficheiro: %s" % file_name)
        print("Tamanho do ficheiro: %s" % os.path.getsize(join_paths))
        print("Última vez que foi modificado: %s" % time.ctime(os.path.getmtime(join_paths)))
        print("Última vez que foi acessado: %s" % time.ctime(os.path.getatime(join_paths)))
        print("Data de criação: %s" % time.ctime(os.path.getctime(join_paths)))
        print("")

    print("Lista de todos os ficheiros na Origem: " + str(origin_list))

    # Dar informação detalhada sobre os ficheiros.


if __name__ == "__main__":

    list_exist_main = []
    origin = "Origem"
    destiny = "Destino"

    terminal_arguments = sys.argv
    arguments_list = terminal_arguments[1:]

    try:
        arguments, values = getopt.getopt(arguments_list, 'vhds',
                                          ["origem=", "destino="])
    except getopt.error as err:
        print("Erro no argumento usado consulte o help: ")
        help()
        sys.exit(2)

    if not arguments_list:

        if not os.path.isdir(origin):
            print("\nO diretorio " + origin + " não existe no seu computador. :(\n")
            sys.exit(2)

        elif not os.path.isdir(destiny):
            try:
                os.mkdir(destiny)

            except OSError as e:
                print("\nO diretorio" + destiny + " não foi criado com sucesso! :(\n")
                sys.exit(2)

            else:
                print("\nO diretorio " + destiny + " foi criado com sucesso! :)\n")

        dir_origin = os.path.abspath(origin)  # Path da origem
        dir_destiny = os.path.abspath(destiny)  # Path do destino
        origin_list_main = os.listdir(origin)  # Lista com ficheiros da origem
        destiny_list_main = os.listdir(destiny)  # Lista com ficheiros do destino
        list_exist_main = []  # Lista usada para retirar os duplicates

        for len_origin in range(0, len(origin_list_main)):
            origin_path_join_main = os.path.join(dir_origin, origin_list_main[len_origin])
            origin_raw_string_main = r"{}".format(origin_list_main[len_origin])

            for len_destiny in range(0, len(destiny_list_main)):
                destiny_path_join_main = os.path.join(dir_destiny, destiny_list_main[len_destiny])
                destiny_raw_string_main = r"{}".format(destiny_list_main[len_destiny])
                destiny_path_join_exist_main = os.path.join(dir_destiny, origin_list_main[len_origin])

                if destiny_raw_string_main == origin_raw_string_main:
                    print("O ficheiro ou diretorio " + str(origin_list_main[len_origin]) + " existe no Destino.")

                    if time.ctime(os.path.getmtime(origin_path_join_main)) > time.ctime(os.path.getmtime(destiny_path_join_main)):
                        list_exist_main.append(str(origin_list_main[len_origin]))

                elif not os.path.exists(destiny_path_join_exist_main):
                    list_exist_main.append(str(origin_list_main[len_origin]))

        without_duplicates = list(set(list_exist_main))

        if without_duplicates:
            for file in without_duplicates:
                src_file = os.path.join(dir_origin, file)  # Faz um join do path da Origem com o do ficheiro
                src_file_destiny = os.path.join(dir_destiny, file)
                copy(src_file, dir_destiny, src_file_destiny)

            print("\nCópia concluída com sucesso! :)")

    for argument, value in arguments:

        if argument in "-s":
            silence_information(origin)

        elif argument in "-h":
            help()

        elif argument in "-d":
            debug(origin, destiny)

        elif argument in "-v":
            detailed_information(origin, destiny)

        elif argument in "--origem":
            origin = value

        elif argument in "--destino":
            destiny = value

