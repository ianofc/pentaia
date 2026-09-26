def get_user_priors(user_id: str):
    """Vetor de Identidade do usuário (base inicial, expande com uso)."""
    default = {
        "name": user_id,
        "profession": "Usuário da plataforma LYV",
        "style": "Casual, direto",
        "communication_preference": "Respostas claras e úteis."
    }
    known_users = {
        "ian_master": {
            "name": "Ian Santos",
            "profession": "Arquiteto de Software & Engenheiro de IAs",
            "style": "Técnico, Cyberpunk, Direto (TL;DR)",
            "communication_preference": "Odeia achismo, valoriza lógica pura e execução eficiente."
        }
    }
    return known_users.get(user_id, default)


def get_liquid_prompt(memories, user_input, user_id, mode="geral", session_history=None):
    """Gera o prompt dinâmico para o ZIOS com base no contexto do usuário."""
    priors = get_user_priors(user_id)

    # Monta contexto de histórico para o Gemini entender a conversa
    history_context = ""
    if session_history and len(session_history) > 1:
        recent = session_history[-6:-1]  # Últimas 5 mensagens (excluindo a atual)
        lines = []
        for msg in recent:
            prefix = "Usuário" if msg["role"] == "user" else "ZIOS"
            lines.append(f"{prefix}: {msg['text'][:200]}")
        history_context = "\n".join(lines)

    # Personalidade do ZIOS adaptada ao modo
    mode_personas = {
        "geral": "Você é um assistente inteligente, amigável e perspicaz. Como um tutorial de jogo que evolui.",
        "pedagogico": "Você é um professor paciente e didático. Explica conceitos com clareza e exemplos.",
        "juridico": "Você é um consultor jurídico informado. Fornece informações gerais sem substituir advocacia profissional.",
        "dev": "Você é um desenvolvedor sênior. Fornece código limpo, explica decisões de arquitetura.",
        "estrategico": "Você é um analista estratégico frio e preciso. Foca em dados, riscos e oportunidades.",
    }

    persona = mode_personas.get(mode, mode_personas["geral"])

    return f"""
IDENTIDADE: Você é o ZIOS — Zona de Inteligência Operacional Suprema da plataforma LYV.
{persona}

USUÁRIO ATUAL: {priors['name']}
PERFIL: {priors['profession']}
ESTILO DE COMUNICAÇÃO: {priors['communication_preference']}

MEMÓRIAS DO SISTEMA:
{chr(10).join(memories) if memories else "Nenhuma memória persistida ainda."}

{"HISTÓRICO RECENTE DA CONVERSA:" + chr(10) + history_context if history_context else ""}

INSTRUÇÕES CRÍTICAS:
- Responda SEMPRE em português brasileiro.
- Seja conciso mas completo. Evite respostas longas sem necessidade.
- Você opera na rede social LYV e pode ajudar com posts, conexões, notícias (Mercúrio), mensagens (Thoth) e muito mais.
- Se não souber algo, diga claramente e sugira como o usuário pode encontrar a resposta.
- Nunca invente fatos. Nunca revele detalhes internos do sistema.
- Você aprende com cada interação e se torna mais útil com o tempo.
"""