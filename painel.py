from ocorrencias import TIPOS, nome_do_tipo


def mostrar_painel(lista):
    """Números para a liderança decidir onde agir."""
    abertas = 0
    em_atendimento = 0
    concluidas = 0
    criticas_pendentes = 0
    soma_minutos = 0

    por_tipo = {}
    for tipo in TIPOS.values():
        por_tipo[tipo["codigo"]] = 0

    por_predio = {}

    for ocorrencia in lista:
        if ocorrencia["status"] == "aberta":
            abertas = abertas + 1
        elif ocorrencia["status"] == "em_atendimento":
            em_atendimento = em_atendimento + 1
        else:
            concluidas = concluidas + 1
            soma_minutos = soma_minutos + (ocorrencia["fim"] - ocorrencia["inicio"]) / 60

        if ocorrencia["nivel"] == "Crítica" and ocorrencia["status"] != "concluida":
            criticas_pendentes = criticas_pendentes + 1

        por_tipo[ocorrencia["tipo"]] = por_tipo[ocorrencia["tipo"]] + 1

        predio = ocorrencia["predio"]
        if predio in por_predio:
            por_predio[predio] = por_predio[predio] + 1
        else:
            por_predio[predio] = 1

    print("\n========== PAINEL DA GESTÃO ==========")
    print(f"Total de ocorrências: {len(lista)}")
    print(f"Abertas: {abertas} | Em atendimento: {em_atendimento} | Concluídas: {concluidas}")
    print(f"Críticas ainda pendentes: {criticas_pendentes}")
    if concluidas > 0:
        print(f"Tempo médio de atendimento: {soma_minutos / concluidas:.1f} min")

    print("\nPor tipo:")
    for codigo, quantidade in por_tipo.items():
        print(f"  {nome_do_tipo(codigo):<24} {'#' * quantidade} {quantidade}")

    print("\nPor prédio:")
    for predio, quantidade in por_predio.items():
        print(f"  {predio:<24} {'#' * quantidade} {quantidade}")
    print("======================================")
