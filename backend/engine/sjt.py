import numpy as np

SJT_KEY = {
    "Q1": {"competency":"Comunicacao","weights":{"A":0.1,"B":0.7,"C":1.0,"D":0.0}},
    "Q2": {"competency":"ResolucaoProblemas","weights":{"A":1.0,"B":0.5,"C":0.2,"D":0.0}},
    "Q3": {"competency":"Lideranca","weights":{"A":1.0,"B":0.4,"C":0.1,"D":0.3}},
    "Q4": {"competency":"Negociacao","weights":{"A":0.3,"B":1.0,"C":0.5,"D":0.2}},
    "Q5": {"competency":"Autogestao","weights":{"A":1.0,"B":0.4,"C":0.2,"D":0.0}},
    "Q6": {"competency":"Criatividade","weights":{"A":1.0,"B":0.3,"C":0.1,"D":0.0}},
    "Q7": {"competency":"GestaoTempo","weights":{"A":1.0,"B":0.3,"C":0.2,"D":0.0}},
    "Q8": {"competency":"AprendizadoAtivo","weights":{"A":1.0,"B":0.2,"C":0.3,"D":0.0}},
    "Q9": {"competency":"Resiliencia","weights":{"A":1.0,"B":0.1,"C":0.2,"D":0.0}},
    "Q10":{"competency":"PensamentoAnalitico","weights":{"A":1.0,"B":0.3,"C":0.2,"D":0.0}},
}

def score_sjt(responses: dict[str,str], key: dict[str,dict] = SJT_KEY):
    comp_scores = {}
    for qid, ans in responses.items():
        meta = key.get(qid)
        if not meta: 
            continue
        comp = meta["competency"]
        w = meta["weights"].get(ans.upper(), 0.0)
        comp_scores[comp] = comp_scores.get(comp, 0.0) + w
    if not comp_scores:
        return {}, 0.0
    maxv = max(comp_scores.values()) or 1.0
    for k in comp_scores:
        comp_scores[k] = round(comp_scores[k]/maxv, 2)
    overall = round(float(np.mean(list(comp_scores.values()))), 2)
    return comp_scores, overall

def infer_softskills(bf: dict[str,float], sjt_comp: dict[str,float]) -> dict:
    potential = {
        "Criatividade": bf["openness"],
        "Implementacao": bf["conscientiousness"],
        "Comunicacao": bf["extraversion"]*0.7 + bf["agreeableness"]*0.3,
        "Resiliencia": (1 - bf["neuroticism"]),
        "TomadaDecisao": bf["conscientiousness"]*0.6 + (1-bf["neuroticism"]) * 0.4,
        "PensamentoAnalitico": bf["conscientiousness"]*0.7 + bf["openness"]*0.3,
        "Negociacao": bf["extraversion"]*0.5 + bf["agreeableness"]*0.5,
        "Lideranca": bf["extraversion"]*0.6 + (1-bf["neuroticism"]) * 0.4,
        "GestaoTempo": bf["conscientiousness"],
        "AprendizadoAtivo": bf["openness"]
    }
    demonstrated = sjt_comp
    return {"potential": potential, "demonstrated": demonstrated}
