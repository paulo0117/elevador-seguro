def notificar_porteiro(ocorrencia):
    print(f"\n[PAINEL DO PORTEIRO] ALERTA: pessoas presas no elevador {ocorrencia['elevador']}, "
          f"andar {ocorrencia['andar']}! (ocorrência #{ocorrencia['id']}, prioridade {ocorrencia['nivel']})")


def avisar_tecnico(ocorrencia, tecnico):
    print(f"[MANUTENÇÃO] {tecnico} foi despachado(a) para a ocorrência #{ocorrencia['id']} "
          f"({ocorrencia['predio']}, elevador {ocorrencia['elevador']}).")


def porteiro_atendeu():
    resposta = input("[PORTEIRO] Atender a chamada? (s/n) ").strip().lower()
    return resposta == "s"
