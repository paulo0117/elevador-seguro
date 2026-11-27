# Elevador Seguro · Central de Ocorrências

Protótipo acadêmico para o Challenge 2026 (FIAP + OTIS): uma ferramenta para **registrar,
classificar, priorizar, despachar e analisar** ocorrências de elevadores.

Quando a ocorrência é **passageiro preso**, entra o Elevador Seguro: o próprio elevador percebe
que travou, abre a ocorrência sozinho e conversa com quem está dentro até o técnico chegar.

## Duas versões

| Versão | Para quê | Como abrir |
| --- | --- | --- |
| Site (`index.html`) | MVP para testar no navegador (deploy no GitHub Pages) | Abrir o arquivo ou o link do deploy |
| Python (`main.py`) | A mesma lógica no terminal, salvando em `ocorrencias.json` | `python main.py` |

## O que o sistema faz

1. **Registra** a ocorrência: prédio, elevador, andar, tipo e descrição.
2. **Classifica** em 4 tipos: passageiro preso, falta de energia, falha técnica, solicitação do cliente.
3. **Prioriza por pontos**: o tipo dá a base (90, 70, 50 ou 20), alguém passando mal soma 30 e elevador parado soma 10.
4. **Despacha** o técnico livre para a ocorrência mais urgente.
5. **Mostra um painel** para a gestão: totais, tempo médio, ocorrências por tipo e por prédio.

## Como rodar o Python

```bash
pip install -r requirements.txt   # opcional: só para a voz
python main.py
```

Sem o `pyttsx3`, o programa funciona igual, só sem falar em voz alta.

## Arquivos Python

| Arquivo | O que faz |
| --- | --- |
| `main.py` | Menu principal e o fluxo do passageiro preso |
| `ocorrencias.py` | Tipos, cálculo de prioridade, fila, técnicos, despacho e conclusão |
| `banco.py` | Lê e grava `ocorrencias.json` |
| `painel.py` | Números para a gestão |
| `elevador.py` | Estado do elevador (finge os sensores) |
| `detector.py` | Percebe que o elevador travou |
| `assistente.py` | Respostas da cabine por palavra-chave (não é IA) |
| `voz.py` | Fala em voz alta e "ouve" o passageiro |
| `porteiro.py` | Avisos para porteiro e manutenção |

## Conteúdo do curso usado

HTML5, CSS e JavaScript (Fases 1 a 3), Bootstrap (Fases 4 e 5), lógica com Python (Fases 1 a 5),
arquivos JSON (Fase 6) e GitHub (Fase 2).
