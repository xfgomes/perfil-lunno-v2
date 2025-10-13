from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import Session
from ..engine.psychometrics import BigFiveScorer
from ..engine.mapping import bigfive_to_disc, infer_archetype
from ..engine.sjt import score_sjt, infer_softskills
from ..engine.narrative import generate_individual_report
from ..models.assessment import Assessment
from ..app import db_engine

bp = Blueprint("reports", __name__, url_prefix="/api/reports")

@bp.post("/score")
@jwt_required()
def score_all():
    data = request.json or {}
    bf_res = BigFiveScorer().score(data.get("bigfive_responses", {})).as_dict()
    disc = bigfive_to_disc(bf_res)
    sjt_comp, sjt_overall = score_sjt(data.get("sjt_responses", {}))
    soft = infer_softskills(bf_res, sjt_comp)
    arch = infer_archetype(bf_res, data.get("motivation", {}))

    payload = {"bigfive": bf_res, "disc": disc, "archetype": arch, "softskills": soft, "sjt": sjt_overall}
    narrative = generate_individual_report(payload)

    ident = get_jwt_identity(); user_id = ident["user_id"]
    with Session(db_engine) as s:
        a = Assessment(user_id=user_id, bigfive=bf_res, disc=disc, archetype=arch, softskills=soft, sjt_score=sjt_overall, narrative_report_individual=narrative)
        s.add(a); s.commit()
        return jsonify({"assessment_id": a.id, **payload, "narrative": narrative})
