import time

# Cada tipo de ocorrência tem um nome para mostrar e um peso de urgência.
TIPOS = {
    "1": {"codigo": "passageiro_preso", "nome": "Passageiro preso", "peso": 90},
    "2": {"codigo": "falta_energia", "nome": "Falta de energia", "peso": 70},
    "3": {"codigo": "falha_tecnica", "nome": "Falha técnica", "peso": 50},
    "4": {"codigo": "solicitacao_cliente", "nome": "Solicitação do cliente", "peso": 20},
}

# Técnicos de campo. No mundo real, viriam do banco de dados.
TECNICOS = ["Ana", "Bruno", "Carla"]


def nome_do_tipo(codigo):
    for tipo in TIPOS.values():
        if tipo["codigo"] == codigo:
            return tipo["nome"]
    return codigo


def calcular_prioridade(codigo_tipo, alguem_mal, elevador_parado):
    """Soma pontos de urgência. Quanto maior, mais na frente da fila."""
    pontos = 0
    for tipo in TIPOS.values():
        if tipo["codigo"] == codigo_tipo:
            pontos = tipo["peso"]

    if alguem_mal:
        pontos = pontos + 30  # risco à saúde vem sempre primeiro
    if elevador_parado:
        pontos = pontos + 10  # elevador fora de uso afeta o prédio todo

    return pontos


def nivel_da_prioridade(pontos):
    if pontos >= 90:
        return "Crítica"
    elif pontos >= 60:
        return "Alta"
    elif pontos >= 40:
        return "Média"
    else:
        return "Baixa"


def nova_ocorrencia(lista, predio, elevador, andar, codigo_tipo, descricao,
                    alguem_mal=False, elevador_parado=True):
    """Cria a ocorrência, calcula a prioridade e coloca na lista."""
    pontos = calcular_prioridade(codigo_tipo, alguem_mal, elevador_parado)
    ocorrencia = {
        "id": len(lista) + 1,
        "data": time.strftime("%d/%m/%Y %H:%M"),
        "predio": predio,
        "elevador": elevador,
        "andar": andar,
        "tipo": codigo_tipo,
        "descricao": descricao,
        "alguem_mal": alguem_mal,
        "prioridade": pontos,
        "nivel": nivel_da_prioridade(pontos),
        "status": "aberta",
        "tecnico": None,
        "atendido_por": None,
        "inicio": time.time(),
        "fim": None,
    }
    lista.append(ocorrencia)
    return ocorrencia


def pegar_prioridade(ocorrencia):
    return ocorrencia["prioridade"]


def fila_de_atendimento(lista):
    """Ocorrências não concluídas, da mais urgente para a menos urgente."""
    pendentes = []
    for ocorrencia in lista:
        if ocorrencia["status"] != "concluida":
            pendentes.append(ocorrencia)
    return sorted(pendentes, key=pegar_prioridade, reverse=True)


def tecnicos_livres(lista):
    """Um técnico está ocupado se tiver uma ocorrência em atendimento."""
    ocupados = []
    for ocorrencia in lista:
        if ocorrencia["status"] == "em_atendimento":
            ocupados.append(ocorrencia["tecnico"])

    livres = []
    for tecnico in TECNICOS:
        if tecnico not in ocupados:
            livres.append(tecnico)
    return livres


def despachar(lista):
    """Manda o primeiro técnico livre para a ocorrência aberta mais urgente."""
    livres = tecnicos_livres(lista)
    if len(livres) == 0:
        return None, None

    for ocorrencia in fila_de_atendimento(lista):
        if ocorrencia["status"] == "aberta":
            ocorrencia["status"] = "em_atendimento"
            ocorrencia["tecnico"] = livres[0]
            return ocorrencia, livres[0]

    return None, None


def concluir(lista, id_ocorrencia):
    for ocorrencia in lista:
        if ocorrencia["id"] == id_ocorrencia and ocorrencia["status"] != "concluida":
            ocorrencia["status"] = "concluida"
            ocorrencia["fim"] = time.time()
            return ocorrencia
    return None
