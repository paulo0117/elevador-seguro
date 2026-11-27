# Estado do elevador. No mundo real, viria dos sensores.
elevador = {
    "andar": 4,
    "em_movimento": True,
    "porta_aberta": False,
    "pessoas_dentro": 2,
}


def travar():
    """Simula a pane: o elevador para entre andares com a porta fechada."""
    elevador["em_movimento"] = False
    elevador["porta_aberta"] = False
    print(">>> [SIMULAÇÃO] O elevador travou entre o 4º e o 5º andar!")
