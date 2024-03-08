def exists_word(word, instance):
    return [
        {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": i + 1}
                for i, line in enumerate(item["linhas_do_arquivo"])
                if word.lower() in line.lower()
            ],
        }
        for item in instance._data
        if any(
            word.lower() in line.lower() for line in item["linhas_do_arquivo"]
        )
    ]


def search_by_word(word, instance):  # nao me parece muito clean
    return [
        {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": i + 1, "conteudo": line}
                for i, line in enumerate(item["linhas_do_arquivo"])
                if word.lower() in line.lower()
            ],
        }
        for item in instance._data
        if any(
            word.lower() in line.lower() for line in item["linhas_do_arquivo"]
        )
    ]
