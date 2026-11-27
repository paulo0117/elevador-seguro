import json

ARQUIVO = "ocorrencias.json"


def carregar():
    """Lê as ocorrências salvas. Se o arquivo ainda não existe, começa vazio."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar(lista):
    """Grava todas as ocorrências no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)
