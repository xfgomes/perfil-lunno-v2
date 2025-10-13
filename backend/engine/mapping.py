def bigfive_to_disc(bf: dict[str,float]) -> dict:
    D = max(0.0, min(1.0, (bf["extraversion"] * (1 - bf["agreeableness"])) * 1.3))
    I = max(0.0, min(1.0, (bf["extraversion"] * bf["agreeableness"]) * 1.2))
    S = max(0.0, min(1.0, ((1 - bf["neuroticism"]) * bf["agreeableness"]) * 1.1))
    C = max(0.0, min(1.0, bf["conscientiousness"]))
    return {"dominance": D, "influence": I, "steadiness": S, "conformity": C}

ARCHETYPES = {
    "Criador": {"motivation":"Inovar, expressar, construir soluções originais","fit":"Autonomia e tolerância ao erro","shadow":"Perfeccionismo, dispersão","signature": lambda bf: bf["openness"]>0.7 and bf["conscientiousness"]>=0.4},
    "Herói": {"motivation":"Desafios e impacto visível","fit":"Alta responsabilidade","shadow":"Competitividade excessiva","signature": lambda bf: bf["extraversion"]>0.65 and bf["neuroticism"]<0.45},
    "Cuidador": {"motivation":"Apoiar pessoas","fit":"Times colaborativos","shadow":"Evitar conflitos","signature": lambda bf: bf["agreeableness"]>0.7 and bf["neuroticism"]<0.6},
    "Sábio": {"motivation":"Conhecimento e precisão","fit":"Ambientes analíticos","shadow":"Paralisia por análise","signature": lambda bf: bf["conscientiousness"]>0.7 and bf["openness"]>0.55},
    "Explorador": {"motivation":"Liberdade e descoberta","fit":"Ambientes dinâmicos","shadow":"Dispersão","signature": lambda bf: bf["openness"]>0.75 and bf["conscientiousness"]<0.5},
    "Governante": {"motivation":"Ordem e liderança responsável","fit":"Estruturas organizadas","shadow":"Rigidez","signature": lambda bf: bf["conscientiousness"]>0.8 and bf["extraversion"]>0.6},
    "Inocente": {"motivation":"Segurança e harmonia","fit":"Ambientes previsíveis","shadow":"Ingenuidade","signature": lambda bf: bf["agreeableness"]>0.75 and bf["neuroticism"]<0.5},
    "Mago": {"motivation":"Transformar ideias em realidade","fit":"Ecossistemas inovadores","shadow":"Arrogância intelectual","signature": lambda bf: bf["openness"]>0.8 and bf["extraversion"]<0.6},
    "Bobo": {"motivation":"Alegrar e quebrar padrões","fit":"Ambientes leves","shadow":"Falta de seriedade","signature": lambda bf: bf["extraversion"]>0.8 and bf["agreeableness"]>0.5},
    "Amante": {"motivation":"Conexão e empatia","fit":"Contextos sensíveis","shadow":"Dependência emocional","signature": lambda bf: bf["agreeableness"]>0.8 and bf["openness"]>0.6},
    "Forasteiro": {"motivation":"Autenticidade e ruptura","fit":"Inovação contestadora","shadow":"Isolamento","signature": lambda bf: bf["openness"]>0.7 and bf["agreeableness"]<0.5},
    "Cuidador Visionário": {"motivation":"Apoiar com visão de futuro","fit":"Times com propósito","shadow":"Idealismo excessivo","signature": lambda bf: bf["agreeableness"]>0.65 and bf["openness"]>0.65},
}

def infer_archetype(bf: dict[str,float], motiv_responses: dict[str,float] | None = None) -> dict:
    candidates = [name for name, spec in ARCHETYPES.items() if spec["signature"](bf)]
    chosen = candidates[0] if candidates else "Sábio"
    meta = ARCHETYPES[chosen]
    return {"name": chosen, "motivation": meta["motivation"], "fit": meta["fit"], "shadow": meta["shadow"]}
