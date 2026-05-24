def explain_agent_flow():
    flow = [
        "1. O usuario solicita uma acao ao agente de IA.",
        "2. O agente interpreta a intencao do usuario.",
        "3. O script Python usa as credenciais do Trello.",
        "4. A API do Trello retorna dados de quadros, listas ou cartoes.",
        "5. O agente usa essas informacoes para apoiar uma decisao ou acao.",
    ]

    return "\n".join(flow)


if __name__ == "__main__":
    print("Fluxo conceitual de um agente de IA integrado ao Trello:")
    print(explain_agent_flow())
