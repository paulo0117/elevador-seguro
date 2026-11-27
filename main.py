from banco import carregar, salvar
from ocorrencias import (TIPOS, nome_do_tipo, nova_ocorrencia, fila_de_atendimento,
                         tecnicos_livres, despachar, concluir)
from painel import mostrar_painel
from elevador import travar
from detector import esperar_travamento
from voz import falar, ouvir
from assistente import MENSAGEM_ABERTURA, responder
from porteiro import notificar_porteiro, avisar_tecnico, porteiro_atendeu

MAX_FALAS = 5  # na simulação, o técnico "chega" depois de 5 falas


# ---------- Gestão de ocorrências ----------

def registrar_ocorrencia(lista):
    print("\n--- Nova ocorrência ---")
    predio = input("Prédio: ").strip()
    elevador = input("Elevador (ex.: A): ").strip().upper()
    andar = input("Andar: ").strip()

    print("Tipo:")
    for numero, tipo in TIPOS.items():
        print(f"  {numero} - {tipo['nome']}")
    escolha = input("Escolha: ").strip()
    while escolha not in TIPOS:
        escolha = input("Opção inválida. Escolha de 1 a 4: ").strip()

    descricao = input("Descrição: ").strip()
    alguem_mal = input("Alguém passando mal? (s/n) ").strip().lower() == "s"
    parado = input("O elevador está parado? (s/n) ").strip().lower() == "s"

    ocorrencia = nova_ocorrencia(lista, predio, elevador, andar, TIPOS[escolha]["codigo"],
                                 descricao, alguem_mal, parado)
    salvar(lista)
    print(f"Ocorrência #{ocorrencia['id']} registrada. Prioridade: {ocorrencia['nivel']} "
          f"({ocorrencia['prioridade']} pontos).")


def mostrar_fila(lista):
    fila = fila_de_atendimento(lista)
    print("\n--- Fila de atendimento (mais urgente primeiro) ---")
    if len(fila) == 0:
        print("Nenhuma ocorrência pendente.")
    for o in fila:
        tecnico = o["tecnico"] if o["tecnico"] else "-"
        print(f"#{o['id']:<3} {o['nivel']:<8} {nome_do_tipo(o['tipo']):<23} "
              f"{o['predio']:<18} elev. {o['elevador']:<3} {o['status']:<15} técnico: {tecnico}")
    print(f"Técnicos livres: {', '.join(tecnicos_livres(lista)) or 'nenhum'}")


def despachar_tecnico(lista):
    ocorrencia, tecnico = despachar(lista)
    if ocorrencia is None:
        print("Nada para despachar: sem ocorrência aberta ou sem técnico livre.")
    else:
        avisar_tecnico(ocorrencia, tecnico)
        salvar(lista)


def concluir_ocorrencia(lista):
    numero = input("Número da ocorrência concluída: ").strip()
    if not numero.isdigit():
        print("Digite só o número.")
        return
    ocorrencia = concluir(lista, int(numero))
    if ocorrencia is None:
        print("Ocorrência não encontrada ou já concluída.")
    else:
        salvar(lista)
        print(f"Ocorrência #{ocorrencia['id']} concluída.")


# ---------- Elevador Seguro: atendimento a passageiro preso ----------

def conversa_com_porteiro():
    print("(Porteiro na linha. Digite 'fim' quando o técnico chegar.)")
    while True:
        fala_do_porteiro = input("[PORTEIRO] ")
        if fala_do_porteiro.lower() == "fim":
            break
        falar(fala_do_porteiro)
        ouvir()


def conversa_com_assistente(ocorrencia, lista):
    for _ in range(MAX_FALAS):
        fala = ouvir()
        resposta, precisa_de_humano = responder(fala)
        falar(resposta)
        if precisa_de_humano:
            # alguém passando mal: a ocorrência sobe de prioridade
            ocorrencia["alguem_mal"] = True
            ocorrencia["prioridade"] = ocorrencia["prioridade"] + 30
            ocorrencia["nivel"] = "Crítica"
            salvar(lista)
            print("[PAINEL DO PORTEIRO] URGENTE: passageiro relatou mal-estar!")
            conversa_com_porteiro()
            return "assistente + porteiro"
    return "assistente"


def simular_elevador_travado(lista):
    input("\nPressione Enter para simular o elevador travando...")
    travar()
    print("Vigiando o elevador...")
    esperar_travamento()

    # o próprio sistema abre a ocorrência, ninguém precisou ligar
    ocorrencia = nova_ocorrencia(lista, "Ed. Aurora", "A", "entre 4 e 5", "passageiro_preso",
                                 "Detectado automaticamente: parado entre andares com pessoas dentro.")
    salvar(lista)

    notificar_porteiro(ocorrencia)
    despachar_tecnico(lista)
    falar(MENSAGEM_ABERTURA)

    if porteiro_atendeu():
        falar("O porteiro está na linha agora.")
        conversa_com_porteiro()
        quem_atendeu = "porteiro"
    else:
        print("(Porteiro não atendeu. O assistente automático continua a conversa.)")
        quem_atendeu = conversa_com_assistente(ocorrencia, lista)

    falar("O técnico chegou e vai abrir a porta. Obrigado pela paciência.")
    ocorrencia["atendido_por"] = quem_atendeu
    concluir(lista, ocorrencia["id"])
    salvar(lista)
    print(f"[REGISTRO] Ocorrência #{ocorrencia['id']} salva em ocorrencias.json")


# ---------- Menu ----------

def main():
    lista = carregar()
    while True:
        print("\n===== OCORRÊNCIAS DE ELEVADORES =====")
        print("1 - Registrar ocorrência")
        print("2 - Ver fila de atendimento")
        print("3 - Despachar técnico para a mais urgente")
        print("4 - Concluir ocorrência")
        print("5 - Painel da gestão")
        print("6 - Simular elevador travado (Elevador Seguro)")
        print("0 - Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            registrar_ocorrencia(lista)
        elif opcao == "2":
            mostrar_fila(lista)
        elif opcao == "3":
            despachar_tecnico(lista)
        elif opcao == "4":
            concluir_ocorrencia(lista)
        elif opcao == "5":
            mostrar_painel(lista)
        elif opcao == "6":
            simular_elevador_travado(lista)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


main()
