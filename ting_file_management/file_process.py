import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)

    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    if dict not in instance._data:  # devo acessar informacoes com underline?
        instance.enqueue(dict)
        print(dict, file=sys.stdout)


def remove(instance):
    if instance.__len__() == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        data = instance.dequeue()
        print(
            f"Arquivo {data['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
