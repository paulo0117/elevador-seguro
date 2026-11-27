import time
from elevador import elevador

TEMPO_LIMITE = 5  # segundos (curto para a demonstração)


def esperar_travamento():
    """Vigia o elevador e só retorna quando detectar alguém preso."""
    parado_desde = None

    while True:
        parado = not elevador["em_movimento"] and not elevador["porta_aberta"]

        if parado:
            if parado_desde is None:
                parado_desde = time.time()  # começou a contar agora
            segundos_parado = time.time() - parado_desde
            if segundos_parado >= TEMPO_LIMITE and elevador["pessoas_dentro"] > 0:
                return True
        else:
            parado_desde = None  # voltou a andar: zera a contagem

        time.sleep(1)  # confere de novo a cada 1 segundo
