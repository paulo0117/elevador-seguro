# Assistente automático da cabine.
# Não é inteligência artificial: são regras com palavras-chave (if, for, dicionário).
# No sistema real, este é o lugar onde entraria uma IA de verdade.

MENSAGEM_ABERTURA = (
    "Olá, aqui é a central do prédio. O elevador parou entre o quarto e o quinto andar. "
    "A portaria e a manutenção já foram avisadas. Vocês estão em segurança. "
    "Alguém está passando mal?"
)

# palavra-chave -> resposta
RESPOSTAS = {
    "porta": "Por favor, não tente abrir a porta. O técnico vai abrir com segurança.",
    "respir": "O ar circula normalmente pela cabine. Respire devagar, você está seguro.",
    "demor": "O técnico já está a caminho. Eu aviso assim que ele chegar.",
    "medo": "É normal sentir medo. Estou aqui com você o tempo todo.",
}

# se aparecer alguma dessas, chama um humano na hora
PALAVRAS_DE_PERIGO = ["passando mal", "estou mal", "desmai", "falta de ar", "grávida"]


def responder(fala):
    """Recebe o que o passageiro disse e devolve (resposta, precisa_de_humano)."""
    if fala.startswith("não") or fala.startswith("ninguém"):
        return "Ótimo. Fiquem tranquilos, a ajuda já está a caminho.", False

    for palavra in PALAVRAS_DE_PERIGO:
        if palavra in fala:
            return "Entendi. Vou chamar uma pessoa agora mesmo para falar com você.", True

    for chave, resposta in RESPOSTAS.items():
        if chave in fala:
            return resposta, False

    return "Entendi. Fique tranquilo, a ajuda já está a caminho.", False
