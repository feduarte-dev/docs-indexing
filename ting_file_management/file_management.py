import sys


def txt_importer(path_file):

    if path_file[-3:] != "txt":
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            lines = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    return lines


print(txt_importer("statics/nomde_pedro.txt"))
