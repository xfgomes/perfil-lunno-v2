from flask import Blueprint, jsonify

bp = Blueprint("items", __name__, url_prefix="/api/items")

@bp.get("/bigfive")
def bf_items():
    items = [{"id": f"BF{i}", "text": f"Afirmativa {i}", "reverse": (i in [3,7,12,28,44])} for i in range(1,61)]
    return jsonify({"items": items})

@bp.get("/sjt")
def sjt_items():
    items = [
        {"id":"Q1","stem":"Seu colega faz críticas negativas à sua apresentação em público. O que você faz?","options":["A","B","C","D"]},
        {"id":"Q2","stem":"Você recebe um projeto com prazo curto e requisitos ambíguos. Sua atitude é:","options":["A","B","C","D"]},
        {"id":"Q3","stem":"Seu time está desmotivado com o ritmo de trabalho. O que você faz?","options":["A","B","C","D"]},
        {"id":"Q4","stem":"Durante uma reunião, há divergência forte entre colegas. Você:","options":["A","B","C","D"]},
        {"id":"Q5","stem":"Você percebe um erro seu em um relatório enviado. Qual é sua reação?","options":["A","B","C","D"]},
        {"id":"Q6","stem":"Seu gestor pede uma solução criativa para um problema recorrente. Você:","options":["A","B","C","D"]},
        {"id":"Q7","stem":"Você tem várias tarefas simultâneas. Qual atitude toma?","options":["A","B","C","D"]},
        {"id":"Q8","stem":"Seu projeto recebeu críticas construtivas. Você:","options":["A","B","C","D"]},
        {"id":"Q9","stem":"Você enfrenta uma situação imprevista e estressante. O que faz?","options":["A","B","C","D"]},
        {"id":"Q10","stem":"Uma equipe pede sua ajuda para resolver um problema técnico. Você:","options":["A","B","C","D"]},
    ]
    return jsonify({"items": items})
